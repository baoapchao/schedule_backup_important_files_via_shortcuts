import shutil
import os
import win32com.client

def resolve_shortcut(shortcut_path):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(shortcut_path)
    return shortcut.TargetPath

def backup_file(source, destination):
    try:
        # Ensure the source file exists
        if not os.path.isfile(source):
            print(f"Source file {source} does not exist.")
            return

        # Ensure the destination directory exists, create if not
        if not os.path.exists(os.path.dirname(destination)):
            os.makedirs(os.path.dirname(destination))

        # Copy the file
        shutil.copy2(source, destination)
        print(f"File {source} backed up to {destination} successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

def backup_files_from_shortcuts(shortcut_folder, backup_folder):
    for filename in os.listdir(shortcut_folder):
        if filename.endswith(".lnk"):
            shortcut_path = os.path.join(shortcut_folder, filename)
            target_path = resolve_shortcut(shortcut_path)
            if os.path.isfile(target_path):
                backup_destination = os.path.join(backup_folder, os.path.basename(target_path))
                backup_file(target_path, backup_destination)
            else:
                print(f"Target file {target_path} does not exist for shortcut {shortcut_path}")

# Example usage
shortcut_folder = 'file_shortcuts'
backup_folder = 'backup_folder'
backup_files_from_shortcuts(shortcut_folder, backup_folder)