import subprocess

def dump_wifi_passwords():
    command = "netsh wlan show profiles"
    profiles = subprocess.check_output(command, shell=True).decode('utf-8').split('\n')

    for profile in profiles:
        if "All User Profile" in profile:
            profile_name = profile.split(":")[1][1:-1]
            print(f"Profile: {profile_name}")
            password_command = f"netsh wlan show profile name=\"{profile_name}\" key=clear"
            password_info = subprocess.check_output(password_command, shell=True).decode('utf-8')
            for line in password_info.split('\n'):
                if "Key Content" in line:
                    print(f"Password: {line.split(':')[1][1:-1]}")

if __name__ == "__main__":
    dump_wifi_passwords()