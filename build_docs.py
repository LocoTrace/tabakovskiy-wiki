diff --git a/build_docs.py b/build_docs.py
index 5204ead083df1b1b48b05fdaab93ac94ee5d9344..6df9685d662a6002fdc55a67a2c5a418059e1eff 100644
--- a/build_docs.py
+++ b/build_docs.py
@@ -1,73 +1,33 @@
 from pathlib import Path
 import shutil
 
-# Manual transliteration table for russian -> latin characters.
-_TRANS_TABLE = {
-    "А": "A", "а": "a",
-    "Б": "B", "б": "b",
-    "В": "V", "в": "v",
-    "Г": "G", "г": "g",
-    "Д": "D", "д": "d",
-    "Е": "E", "е": "e",
-    "Ё": "E", "ё": "e",
-    "Ж": "Zh", "ж": "zh",
-    "З": "Z", "з": "z",
-    "И": "I", "и": "i",
-    "Й": "I", "й": "i",
-    "К": "K", "к": "k",
-    "Л": "L", "л": "l",
-    "М": "M", "м": "m",
-    "Н": "N", "н": "n",
-    "О": "O", "о": "o",
-    "П": "P", "п": "p",
-    "Р": "R", "р": "r",
-    "С": "S", "с": "s",
-    "Т": "T", "т": "t",
-    "У": "U", "у": "u",
-    "Ф": "F", "ф": "f",
-    "Х": "Kh", "х": "kh",
-    "Ц": "Ts", "ц": "ts",
-    "Ч": "Ch", "ч": "ch",
-    "Ш": "Sh", "ш": "sh",
-    "Щ": "Shch", "щ": "shch",
-    "Ы": "Y", "ы": "y",
-    "Э": "E", "э": "e",
-    "Ю": "Yu", "ю": "yu",
-    "Я": "Ya", "я": "ya",
-    "Ь": "", "ь": "",
-    "Ъ": "", "ъ": "",
-}
+"""Simple utility to copy Markdown files from ``base`` to ``docs``.
+
+The previous version of this script performed transliteration of file and
+directory names.  This resulted in broken links and made it impossible to keep
+the original Cyrillic names used in Obsidian.  The script now preserves the
+original names and only skips hidden files and directories.
+"""
 
 SOURCE = Path("base")
 TARGET = Path("docs")
 
-def transliterate(name: str) -> str:
-    """Transliterate cyrillic characters and normalise spaces."""
-    result = []
-    for ch in name:
-        if ch == " ":
-            result.append("_")
-        else:
-            result.append(_TRANS_TABLE.get(ch, ch))
-    return "".join(result)
-
 def copy_dir(src: Path, dst: Path):
     for item in src.iterdir():
         if item.name.startswith('.'):
             # Skip hidden directories and files like .obsidian
             continue
-        new_name = transliterate(item.name)
-        dst_item = dst / new_name
+        dst_item = dst / item.name
         if item.is_dir():
             dst_item.mkdir(parents=True, exist_ok=True)
             copy_dir(item, dst_item)
         elif item.suffix.lower() == ".md":
             dst_item.parent.mkdir(parents=True, exist_ok=True)
             shutil.copy2(item, dst_item)
 
 if TARGET.exists():
     shutil.rmtree(TARGET)
 TARGET.mkdir()
 
 copy_dir(SOURCE, TARGET)
-print("✅ Готово: файлы скопированы с транслитерацией в папку docs")
+print("✅ Готово: файлы скопированы в папку docs")
