import psutil
import time

def log_system_usage():
    while True:
        cpu_usage = psutil.cpu_percent()
        memory_info = psutil.virtual_memory()
        with open("system_usage_log.txt", "a") as f:
            f.write(f"CPU Usage: {cpu_usage}%, Memory Usage: {memory_info.percent}%\n")
        time.sleep(60)  # Log every minute

if __name__ == "__main__":
    log_system_usage()