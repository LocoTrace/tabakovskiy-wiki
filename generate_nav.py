from pathlib import Path
import re

def generate_nav_structure(base_dir: Path, docs_prefix="docs") -> str:
    def walk_dir(path: Path, indent: int = 2) -> str:
        yaml = ""
        items = sorted(path.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
        for item in items:
            prefix = "  " * indent
            if item.is_dir():
                yaml += f"{prefix}- {item.name}:\n"
                yaml += walk_dir(item, indent + 1)
            elif item.suffix == ".md":
                relative_path = f"{docs_prefix}/{item.relative_to(base_dir).as_posix()}"
                yaml += f"{prefix}- {item.stem}: {relative_path}\n"
        return yaml

    return "nav:\n" + walk_dir(base_dir)

def replace_nav_block(yml_path: Path, new_nav: str):
    content = yml_path.read_text(encoding="utf-8")

    # Резервная копия
    yml_path.with_suffix(".yml.bak").write_text(content, encoding="utf-8")

    # Заменяем nav
    new_content = re.sub(r"\nnav:\n.*?(?=\n\w|$)", "\n" + new_nav.rstrip(), content, flags=re.DOTALL)

    yml_path.write_text(new_content, encoding="utf-8")
    print("✅ nav обновлён в mkdocs.yml")

def main():
    base = Path("base")
    nav_yaml = generate_nav_structure(base)
    mkdocs_path = Path("mkdocs.yml")

    replace_nav_block(mkdocs_path, nav_yaml)

if __name__ == "__main__":
    main()
