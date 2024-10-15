import os

def erase_partition(drive_letter):
    os.system(f"format {drive_letter}: /Q /Y")
    print(f"Partition {drive_letter}: erased.")

if __name__ == "__main__":
    drive_letter = 'C'  # Change to desired drive
    erase_partition(drive_letter)