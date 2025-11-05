"""
Simuliert einen Dateiparser (Dateiname, Endung, Typ)
"""

from pathlib import Path
from typing import NamedTuple

class FileInfo(NamedTuple):
    name: str
    suffix: str
    type: str


def parse(filename: str | Path) -> FileInfo:
    """Parse file information using pathlib"""
    path = Path(filename)
    if not path.exists() or not path.is_file():
        raise FileNotFoundError(f"{filename} not found")
    
    suffix = path.suffix.lstrip('.')
    return FileInfo(
        name=path.stem,
        suffix=path.suffix,
        type=suffix.lower() if suffix else 'Unknown Filetype'
    )