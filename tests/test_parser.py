from pathlib import Path
from fileparser.parser import parse, FileInfo

def test_parse_valid_file(tmp_path: Path):
    testfile = tmp_path / "beispiel.txt"
    testfile.write_text("hello")
    info = parse(str(testfile))
    assert isinstance(info, FileInfo)
    assert info.name == "beispiel"
    assert info.suffix == ".txt"
    assert info.type == "txt"