from pathlib import Path
import re

def get_title(md_file: Path) -> str:
    """Вернёт первый заголовок # из .md-файла или имя файла, если нет заголовка."""
    try:
        for line in md_file.read_text(encoding="utf-8").splitlines():
            if line.startswith("#"):
                return line.lstrip("#").strip()
    except Exception:
        pass
    return md_file.stem

def generate_nav_structure(base_dir: Path) -> str:
    """Создаёт YAML-блок nav для mkdocs, проходя по всем .md-файлам и папкам."""
    def walk_dir(path: Path, indent: int = 2) -> str:
        yaml = ""
        items = sorted(path.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
        for item in items:
            if item.name.startswith('.'):
                continue
            prefix = "  " * indent
            if item.is_dir():
                yaml += f"{prefix}- {item.name}:\n"
                yaml += walk_dir(item, indent + 1)
            elif item.suffix.lower() == ".md":
                relative_path = item.relative_to(base_dir).as_posix()
                title = get_title(item)
                yaml += f"{prefix}- {title}: {relative_path}\n"
        return yaml

    return "nav:\n" + walk_dir(base_dir)

def replace_nav_block(yml_path: Path, new_nav: str):
    """Заменяет существующий nav: в mkdocs.yml на новый. Делает бэкап."""
    content = yml_path.read_text(encoding="utf-8")
    yml_path.with_suffix(".yml.bak").write_text(content, encoding="utf-8")  # backup
    new_content = re.sub(r"\nnav:\n.*?(?=\n\w|$)", "\n" + new_nav.rstrip(), content, flags=re.DOTALL)
    yml_path.write_text(new_content, encoding="utf-8")
    print("✅ nav обновлён в mkdocs.yml")

def main():
    docs = Path("docs")
    nav_yaml = generate_nav_structure(docs)
    mkdocs_path = Path("mkdocs.yml")
    replace_nav_block(mkdocs_path, nav_yaml)

if __name__ == "__main__":
    main()
