# TreeGen

**TreeGen** is a cross-platform CLI utility that creates real folder and file structures from plain-text blueprints.
It supports tree-style, flat-style, and full-path formats, making it ideal for quickly scaffolding projects.
You can write your own structure file or generate one using ChatGPT—TreeGen brings it to life in seconds.

---

## Features

- **Supports multiple structure formats:**  
  - Tree-style (with `├──`, `│`, `└──` symbols and indentation)
  - Flat-style (directory, then files, no indentation)
  - Full-path style (e.g., `project/src/main.py`)
- **Handles nested directories and files**
- **Ignores comments and blank lines**
- **Creates empty files and folders as specified**
- **Cross-platform (works on Windows, macOS, Linux)**

---

## Example Usage

### 1. Create a structure file

Example: `my-structure.txt`
```
my-app/
├── backend/
│   ├── app.py
│   └── db/
│       └── connection.py
├── frontend/
│   └── src/
│       └── App.jsx
└── README.md
```

### 2. Run TreeGen

```sh
python structuregen.py my-structure.txt
```

---

## Installation

No installation required!  
Just download `structuregen.py` and run with Python 3.6+.

---

## Releases

Pre-built binaries are available for both **Windows** and **Linux** — no Python required!

### 🔽 Download from Releases
Grab the latest release from the [Releases](https://github.com/your-username/TreeGen/releases) page:

- **Windows**: `treegen.exe`
- **Linux**: `treegen` (make sure it’s executable)

### 🛠 How to Use

#### On Windows:
```powershell
.\treegen.exe my-structure.txt
```

#### On Linux:
```
chmod +x treegen
./treegen my-structure.txt
```
You can now scaffold your directory structure instantly without needing to install Python.

## Structure File Syntax

- **Directories:** End with `/`
- **Files:** Any line with a filename (e.g., `main.py`)
- **Tree symbols and indentation:** Supported but not required
- **Full paths:** Supported (e.g., `my-app/src/main.py`)
- **Comments:** Lines starting with `#` or after `#` on a line are ignored

---

## Example Structure Files

### Tree-style
```
project/
├── src/
│   └── main.py
└── README.md
```

### Flat-style
```
project/
src/
main.py
README.md
```

### Full-path style
```
project/
project/src/main.py
project/README.md
```

---

## License

MIT License

---

## Author

Generated with by GitHub Copilot 


