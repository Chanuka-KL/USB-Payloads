import os
import time

def monitor_logins():
    while True:
        os.system('tasklist | findstr "login.exe"')  # Replace with the actual process
        time.sleep(5)

if __name__ == "__main__":
    monitor_logins()