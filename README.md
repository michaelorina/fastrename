# FastRename – Bulk File Renaming CLI Tool

**FastRename** is a sleek and simple command-line tool to bulk rename files with prefix, suffix, numbering, replacements, extension filters, dry-run support, undo, and colorful output — all in one fast Python script.

## Features
- Add prefix and suffix to filenames
- Replace text in filenames
- Auto-numbering with custom start
- Filter by file extension
- Dry-run mode (simulate changes before renaming)
- Undo renaming with backup
- Colorful terminal output

## Usage
```bash
python fastrename.py [options] directory
```
## Examples:
```bash
python fastrename.py ./files --prefix new_
python fastrename.py ./files --suffix _done
python fastrename.py ./files --replace old new
python fastrename.py ./files --start-number 100
python fastrename.py ./files --extension .txt
python fastrename.py ./files --dry-run
```
## Undo Last Renaming
```bash
python fastrename.py ./files --undo
```

## Setup
``` bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run Tests
```bash
pytest tests/
```
This was my **Thursday Build Project** — I do this on Fiverr too!  
Need custom CLI tools or scripts? Hire me on Fiverr: [https://www.fiverr.com/s/dDBDPm0](https://www.fiverr.com/s/dDBDPm0)
