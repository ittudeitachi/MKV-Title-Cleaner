# MKV Title Cleaner

[![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/ittudeitachi/MKV-Title-Cleaner/blob/main/LICENSE)
[![Release](https://img.shields.io/github/v/release/ittudeitachi/MKV-Title-Cleaner)](https://github.com/ittudeitachi/MKV-Title-Cleaner/releases)

🧹 A lightweight Python script to recursively remove the `title` metadata from `.mkv` files using `mkvpropedit` from the [MKVToolNix](https://mkvtoolnix.download/) suite.

---

## 📦 Installation

### Requirements

- [Python 3.6+](https://www.python.org/)
- [MKVToolNix](https://mkvtoolnix.download/) (specifically `mkvpropedit.exe`)

### Setup

1. Install MKVToolNix and ensure `mkvpropedit.exe` is available on your system.
2. Clone this repository or download the script.

```bash
git clone https://github.com/ittudeitachi/mkv-title-cleaner.git
cd mkv-title-cleaner
```

3. Open `main.py` and configure your paths:

```python
mkvpropedit_path = r"C:\Program Files\MKVToolNix\mkvpropedit.exe"
root_dir = r"C:\Path\To\Your\MKV\Files"
```

---

## ▶️ Usage

Run the script from terminal or within PyCharm:

```bash
python main.py
```

It will:
- Recursively scan `root_dir` and subfolders
- Identify `.mkv` files
- Remove the `title` metadata using `mkvpropedit` (without remuxing)

---

## 🧾 Output Example

```
🔄 Removing title from: C:\Movies\Action\movie1.mkv
🔄 Removing title from: C:\Movies\Drama\episode2.mkv
✅ Done.
```

---

## 💡 Why Use This?

- Clean `.mkv` files with unwanted embedded titles
- Fast, non-destructive metadata editing (no remuxing)
- Useful for organizing large media libraries

---

## 🪪 License

This project is licensed under the **MIT License**  
See the [LICENSE](LICENSE) file for full details.

> You must include attribution to the original project:  
> **"MKV Title Cleaner by Ibrahim Irusham Rashad"** in your documentation or user interface if you distribute this software or any derivative work.

---

## 🙏 Acknowledgments

- [MKVToolNix](https://mkvtoolnix.download/) — particularly mkvpropedit, the core utility enabling fast, in-place MKV metadata editing.

> This project is not affiliated with or endorsed by MKVToolNix. This tool is for educational and personal use only.