import sys
from winreg import *

reg_path = r"SYSTEM\CurrentControlSet\Control\StorageDevicePolicies"
key = CreateKeyEx(HKEY_LOCAL_MACHINE, reg_path)

def set_WriteProtect():
    try:
        SetValueEx(key, 'WriteProtect',0,REG_DWORD,0x1)
        print("[+] Turn On Write Protection")
        print('[+] WriteProtect Value: 0x01 Type:REG_DWORD')
    except:
        print("[!] Permission denied!")

def unset_WriteProtect():
    try: 
        SetValueEx(key, 'WriteProtect',0,REG_DWORD,0x0)
        print("[+] Turn Off Write Protection")
        print('[+] WriteProtect Value: 0x00 Type:REG_DWORD')
    except:
        print("[!] Permission denied!")

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ('0','1'):
        print('''[!]Usage: (Turn On) WriteProtect.py 1
          (Turn Off) WriteProtect.py 0''')
    elif sys.argv[1] == '1':
        set_WriteProtect()
    else:
        unset_WriteProtect()

if __name__=="__main__":
    main()
