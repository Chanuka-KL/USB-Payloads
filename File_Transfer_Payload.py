import os
import shutil

def transfer_files(source_directory, target_directory):
    for filename in os.listdir(source_directory):
        if filename.endswith('.txt') or filename.endswith('.docx'):
            shutil.copy(os.path.join(source_directory, filename), target_directory)
            print(f"Transferred: {filename}")

if __name__ == "__main__":
    source_dir = r'C:\path\to\source\directory'
    target_dir = r'E:\path\to\usb\drive'  # Change to the actual USB drive letter
    transfer_files(source_dir, target_dir)