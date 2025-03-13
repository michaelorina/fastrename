import os
import argparse
import shutil
from colorama import Fore, Style, init

init(autoreset=True)

BACKUP_DIR = ".fastrename_backup"

def rename_files(directory, prefix=None, suffix=None, replace=None, start_number=None, extension=None, dry_run=False):
    files = os.listdir(directory)
    files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
    if extension:
        files = [f for f in files if f.lower().endswith(extension.lower())]

    if not files:
        print(Fore.YELLOW + "⚠ No matching files found.")
        return

    # Create backup
    backup_path = os.path.join(directory, BACKUP_DIR)
    if not dry_run:
        os.makedirs(backup_path, exist_ok=True)

    for index, filename in enumerate(files):
        old_path = os.path.join(directory, filename)
        name, ext = os.path.splitext(filename)

        new_name = name
        if replace:
            new_name = new_name.replace(replace[0], replace[1])
        if prefix:
            new_name = prefix + new_name
        if suffix:
            new_name = new_name + suffix
        if start_number is not None:
            new_name = f"{start_number + index}_{new_name}"

        new_path = os.path.join(directory, new_name + ext)

        print(Fore.CYAN + f"{filename} → {new_name + ext}")

        if not dry_run:
            shutil.copy2(old_path, os.path.join(backup_path, filename))
            os.rename(old_path, new_path)

    if dry_run:
        print(Fore.YELLOW + "🚫 Dry run mode: No files were actually renamed.")
    else:
        print(Fore.GREEN + "✅ Rename completed. Backup stored in .fastrename_backup")

def main():
    parser = argparse.ArgumentParser(description="FastRename - Bulk file renamer")
    parser.add_argument("directory", help="Directory containing files to rename")
    parser.add_argument("--prefix", help="Prefix to add to filenames")
    parser.add_argument("--suffix", help="Suffix to add to filenames")
    parser.add_argument("--replace", nargs=2, metavar=('OLD', 'NEW'), help="Replace substring in filenames")
    parser.add_argument("--start-number", type=int, help="Add numbers to files starting from this number")
    parser.add_argument("--extension", help="Only rename files with this extension (e.g. .txt)")
    parser.add_argument("--dry-run", action="store_true", help="Preview renaming without making changes")

    args = parser.parse_args()
    rename_files(
        args.directory,
        prefix=args.prefix,
        suffix=args.suffix,
        replace=args.replace,
        start_number=args.start_number,
        extension=args.extension,
        dry_run=args.dry_run
    )

if __name__ == "__main__":
    main()
