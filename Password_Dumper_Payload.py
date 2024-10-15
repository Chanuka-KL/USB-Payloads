import os

def dump_browser_passwords():
    os.system("rundll32.exe keymgr.dll,KRShowKeyMgr")
    print("Password manager opened.")

if __name__ == "__main__":
    dump_browser_passwords()