# 🛠 Codex Task — MkDocs Setup for "Табаковский"

## 🎯 Goal

Generate a fully working MkDocs-based documentation site for the internal knowledge base "Табаковский", based on Obsidian-style Markdown files.

---

## 📂 Project Structure

tabakovskiy-wiki/
├── base/ # Obsidian Markdown files (mostly in Cyrillic)
├── docs/ # Target folder for site generation (may be empty)
├── mkdocs.yml # MkDocs config (needs nav)
├── build_docs.py # Script to copy from base → docs
├── generate_nav.py # Script to create nav structure (to be fixed)

markdown
Копировать
Редактировать

---

## ⚠️ Problems to Fix

1. Files and folders are named in **Cyrillic**, which may break URL references.
2. `mkdocs.yml` has **no valid nav structure**.
3. Scripts `generate_nav.py` and `build_docs.py` work partially or inconsistently.
4. `mkdocs serve` starts, but the pages are 404 or show broken links.

---

## ✅ What Codex Should Do

1. **Read the directory tree inside `base/`**.
2. **Generate a proper `nav:` section** for `mkdocs.yml`:
   - Preserve the original Cyrillic names in the display.
   - Use proper relative paths from `docs/`, respecting folder structure.
3. **Copy all `.md` files from `base/` into `docs/`**, retaining folder hierarchy.
4. Ensure that **links and headings are human-readable (Cyrillic OK)**.
5. Ensure that **`mkdocs serve` works** and the site builds without errors.
6. Commit the changes:
git add .
git commit -m "feat: generated mkdocs nav and linked docs content"
git push origin main

yaml
Копировать
Редактировать

---

## 🧪 Validation Checklist

- [ ] All `.md` files from `base/` appear under `docs/`.
- [ ] Cyrillic titles appear in sidebar.
- [ ] Navigation matches folder structure.
- [ ] `mkdocs serve` runs and site is accessible on `127.0.0.1:8000`.
- [ ] Internal links between pages work.

---

💡 Do not rename files. Preserve Cyrillic filenames and folder names.  
🌐 Goal is to make the site readable and browsable by staff, matching how it looks in Obsidian.