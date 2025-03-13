import os
import shutil
import tempfile
import pytest
from fastrename import rename_files, BACKUP_DIR

@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir

@pytest.fixture
def create_files(temp_dir):
    filenames = ["file1.txt", "file2.txt", "test_file3.txt"]
    for name in filenames:
        with open(os.path.join(temp_dir, name), 'w') as f:
            f.write("test")
    return filenames

def test_prefix_renaming(temp_dir, create_files):
    if not os.path.isdir(temp_dir):
        print(f"[!] Directory '{temp_dir}' does not exist. Please check the path.")
        return
    rename_files(temp_dir, prefix="new_")
    renamed = os.listdir(temp_dir)
    assert any(f.startswith("new_") for f in renamed)

def test_suffix_renaming(temp_dir, create_files):
    if not os.path.isdir(temp_dir):
        print(f"[!] Directory '{temp_dir}' does not exist. Please check the path.")
        return
    rename_files(temp_dir, suffix="_done")
    renamed = os.listdir(temp_dir)
    assert any(f.endswith("_done.txt") for f in renamed)

def test_replace_renaming(temp_dir, create_files):
    if not os.path.isdir(temp_dir):
        print(f"[!] Directory '{temp_dir}' does not exist. Please check the path.")
        return
    rename_files(temp_dir, replace=("file", "doc"))
    renamed = os.listdir(temp_dir)
    assert any("doc" in f for f in renamed)

def test_start_numbering(temp_dir, create_files):
    if not os.path.isdir(temp_dir):
        print(f"[!] Directory '{temp_dir}' does not exist. Please check the path.")
        return
    rename_files(temp_dir, start_number=100)
    renamed = os.listdir(temp_dir)
    assert any(f.startswith("100_") for f in renamed)

def test_extension_filter(temp_dir, create_files):
    if not os.path.isdir(temp_dir):
        print(f"[!] Directory '{temp_dir}' does not exist. Please check the path.")
        return
    # Create a file with different extension
    with open(os.path.join(temp_dir, "note.md"), 'w') as f:
        f.write("test")
    rename_files(temp_dir, prefix="doc_", extension=".txt")
    renamed = os.listdir(temp_dir)
    assert "doc_note.md" not in renamed

def test_dry_run_mode(temp_dir, create_files):
    if not os.path.isdir(temp_dir):
        print(f"[!] Directory '{temp_dir}' does not exist. Please check the path.")
        return
    original_files = os.listdir(temp_dir)
    rename_files(temp_dir, prefix="dryrun_", dry_run=True)
    after_files = os.listdir(temp_dir)
    assert sorted(original_files) == sorted(after_files)

def test_backup_created(temp_dir, create_files):
    if not os.path.isdir(temp_dir):
        print(f"[!] Directory '{temp_dir}' does not exist. Please check the path.")
        return
    rename_files(temp_dir, prefix="bkp_")
    backup_path = os.path.join(temp_dir, BACKUP_DIR)
    assert os.path.exists(backup_path)
    assert len(os.listdir(backup_path)) == len(create_files)