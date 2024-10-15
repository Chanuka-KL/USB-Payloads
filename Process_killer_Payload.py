import os

def kill_process(process_name):
    os.system(f"taskkill /f /im {process_name}")
    print(f"Process {process_name} terminated.")

if __name__ == "__main__":
    process_name = 'antivirus.exe'  # Replace with actual process name
    kill_process(process_name)