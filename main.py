
import os as os
import shutil as shutil



def copy_directory_to_location(source: str, target: str):
    abs_src = os.path.abspath(source)
    abs_target = os.path.abspath(target)
    if os.path.exists(abs_target):
        shutil.rmtree(abs_target)
    os.mkdir(abs_target) # initial call - make the initial directory there (it will be deleted first)
    
    try:
        with os.scandir(abs_src) as entries:
            for entry in entries:
                entry_path = entry.path #this is absolute because scandir is fed an abs path
                target_path = abs_target + entry.name
                if entry_path.is_file():
                    shutil.copy(entry_path, target_path)
                    print(f"File: {entry.name}")
                elif entry_path.is_dir():
                    copy_directory_to_location(entry_path, target_path)
                else:
                    print(f"Other: {entry_path.name}")
    except FileNotFoundError:
        print(f"Error: Directory '{source}' not found.")

    except Exception as e:
        print(f"An error occurred: {e}")
        
    return

def main():
   copy_directory_to_location("src", "public")
    

if __name__ == "__main__":
    main()