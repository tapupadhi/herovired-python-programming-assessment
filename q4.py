import os
import sys
import shutil
from datetime import datetime


def get_unique_name(dest_path):
    if not os.path.exists(dest_path):
        return dest_path
    base, ext = os.path.splitext(dest_path)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{base}_{timestamp}{ext}"


def backup(source_dir, dest_dir):
    if not os.path.isdir(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    if not os.path.isdir(dest_dir):
        print(f"Error: Destination directory '{dest_dir}' does not exist.")
        return

    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        dest_path = os.path.join(dest_dir, item)

        try:
            if os.path.isfile(source_path):
                dest_path = get_unique_name(dest_path)
                shutil.copy2(source_path, dest_path)
                print(f"Copied file: {item} → {os.path.basename(dest_path)}")
            elif os.path.isdir(source_path):
                dest_path = get_unique_name(dest_path)
                shutil.copytree(source_path, dest_path)
                print(f"Copied directory: {item} → {os.path.basename(dest_path)}")
        except Exception as e:
            print(f"Failed to copy '{item}': {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Usage: python backup.py "/path/to/source" "/path/to/destination'"")
    else:
        source = sys.argv[1]
        destination = sys.argv[2]
        backup(source, destination)
