import os
import shutil
import argparse

def copy_dirs(src, dest='dist'):
    try:
        os.makedirs(dest, exist_ok=True)
        recursive_dir_copy(src, dest)
        print("Coping finished successfully.")
    except Exception as e:
        print(f"Some error during coping: {e}")

def recursive_dir_copy(source, destination):
    for item in os.listdir(source):
        item_path = os.path.join(source, item)
        if os.path.isdir(item_path):
            recursive_dir_copy(item_path, destination)
        elif os.path.isfile(item_path):
            copy_file(item_path, destination)

def copy_file(file_path, dir_dest):
    try:
        file_ext = os.path.splitext(file_path)[1][1:]
        subdir_dest = os.path.join(dir_dest, file_ext)

        os.makedirs(subdir_dest, exist_ok=True)
        shutil.copy(file_path, subdir_dest)
        print(f"Copied {file_path} to {subdir_dest}")
    except Exception as e:
        print(f"Error in copying process {file_path}: {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="Path to the source directory")
    parser.add_argument("destination", nargs="?", default="dist", help="Path to the destination directory (default is 'dist')")
    args = parser.parse_args()

    copy_dirs(args.source, args.destination)

if __name__ == "__main__":
    main()
