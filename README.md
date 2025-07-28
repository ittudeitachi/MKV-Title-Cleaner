# MKV Title Cleaner

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

## 📜 License

This project is licensed under the **MIT License** (with attribution clause).  
If you distribute this software or derivative works, you must include attribution to the original project:

> _"MKV Title Cleaner by Ibrahim Irusham Rashad"_ in your documentation or user interface.

See [LICENSE](LICENSE) for full details.
