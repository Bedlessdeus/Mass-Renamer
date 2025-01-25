# Mass Renamer
A simple python script to mass rename files, with a randomly generated UUIDv4, while maintaining file endings.

## Dependencies
- OS
- uuid

## Installation
```bash
pip install uuid
```

## Usage
```bash
py main.py
```

## Known Problems
- The script will not work if the file is in use by another program.
- The script will not work if the file is in a read-only directory.
- If the filename is too long, the script will print an error, this seems to be a problem with windows
