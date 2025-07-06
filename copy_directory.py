import os
import shutil

def copy_item(entry: os.DirEntry[str], target_path:str):
    entry_path = entry.path #this is absolute because scandir is fed an abs path
    target_path = os.path.join(target_path,entry.name)
    if entry.is_file():
        shutil.copy(entry_path, target_path)
        print(f"File: {entry.name}")
    elif entry.is_dir():
        os.makedirs(target_path, exist_ok=True)
        copy_directory_helper(entry_path, target_path)
    else:
        print(f"Other: {entry.name}")
    return

def copy_directory_helper(source:str, target:str):
    try:
        with os.scandir(source) as entries: #get items in the source directory
            for entry in entries:
                copy_item(entry,target) #copy them one by one
    except FileNotFoundError:
        print(f"Error: Directory '{source}' not found.")

    except Exception as e:
        print(f"An error occurred: {e}")
        
    return


def copy_directory_to_location(source: str, target: str):
    abs_src = os.path.abspath(source)
    abs_target = os.path.abspath(target)
    if os.path.exists(abs_target):
        shutil.rmtree(abs_target)
    return copy_directory_helper(abs_src,abs_target)
