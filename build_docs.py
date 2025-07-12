from pathlib import Path
import shutil
from unidecode import unidecode

SOURCE = Path("base")
TARGET = Path("docs")

def transliterate(name: str) -> str:
    return unidecode(name).replace(" ", "_")

def copy_dir(src: Path, dst: Path):
    for item in src.iterdir():
        new_name = transliterate(item.name)
        dst_item = dst / new_name
        if item.is_dir():
            dst_item.mkdir(parents=True, exist_ok=True)
            copy_dir(item, dst_item)
        elif item.suffix == ".md":
            dst_item.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, dst_item)

if TARGET.exists():
    shutil.rmtree(TARGET)
TARGET.mkdir()

copy_dir(SOURCE, TARGET)
print("✅ Готово: файлы скопированы с транслитерацией в папку docs")
