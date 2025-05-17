## Overview

**TreeGen** is a lightweight, cross-platform CLI utility that transforms plain-text blueprints into actual folder and file structures. Perfect for vibe-coders who want to quickly scaffold projects without tedious manual creation.

Whether you prefer tree-style notation, flat structures, or full-path formats, TreeGen handles it all with ease. Generate your structure with AI tools like ChatGPT or write your own—TreeGen brings it to life in seconds.

## ✨ Features

- **Multiple Structure Formats**
  - 🌿 Tree-style (with `├──`, `│`, `└──` symbols and indentation)
  - 📋 Flat-style (simple lists with no indentation)
  - 🛣️ Full-path style (e.g., `project/src/main.py`)
- **Advanced Capabilities**
  - 📁 Handles deeply nested directories
  - 📄 Creates empty files as specified
  - 💬 Ignores comments and blank lines
  - 🖥️ Works across Windows, macOS, and Linux

## 🚀 Getting Started

### Installation

**No installation required!**

- **Python Users**: Download `structuregen.py` and run with Python 3.6+
- **Non-Python Users**: Download pre-built binaries from [Releases](https://github.com/your-username/TreeGen/releases)

### Quick Start

1. **Create a structure file** (e.g., `project-structure.txt`):
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

2. **Run TreeGen**:
   ```sh
   # Using Python
   python structuregen.py project-structure.txt
   
   # Using binary (Windows)
   .\treegen.exe project-structure.txt
   
   # Using binary (Linux/macOS)
   ./treegen project-structure.txt
   ```

3. **Watch your structure come to life!**

## 📋 Structure File Syntax

TreeGen is flexible and accepts several notation formats:

### Tree-style (traditional)
```
project/
├── src/
│   └── main.py
└── README.md
```

### Flat-style (simple)
```
project/
src/
main.py
README.md
```

### Full-path style (explicit)
```
project/
project/src/main.py
project/README.md
```

**Syntax Rules**:
- Directories must end with `/`
- Lines starting with `#` are treated as comments
- Inline comments after `#` are ignored
- Blank lines are skipped

## 📦 Releases

Pre-built binaries are available for:
- **Windows**: `treegen.exe`
- **Linux**: `treegen` (executable)

### Binary Usage

#### Windows:
```powershell
.\treegen.exe my-structure.txt
```

#### Linux:
```bash
chmod +x treegen
./treegen my-structure.txt
```

## 📝 License

This project is licensed under the [MIT License](LICENSE).

## 👨‍💻 Author & Contact

Developed by [Arun](https://linkedin.com/in/0xarun) (Github Copilot) 

[![Follow on X](https://img.shields.io/badge/follow-%400xarun-1DA1F2?logo=x&style=social)](https://x.com/0xarun)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=social&logo=linkedin)](https://linkedin.com/in/0xarun)
