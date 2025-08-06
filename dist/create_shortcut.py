# create_shortcut.py

import os
from win32com.client import Dispatch

def create_shortcut(target_path, shortcut_name="QR Generator", icon_path=None):
    desktop = os.path.join(os.environ["USERPROFILE"], "OneDrive", "Desktop")  # Or use expanduser("~/Desktop")
    shortcut_path = os.path.join(desktop, f"{shortcut_name}.lnk")
    print(f"Creating shortcut at: {shortcut_path}")

    shell = Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = target_path
    shortcut.WorkingDirectory = os.path.dirname(target_path)
    if icon_path:
        shortcut.IconLocation = icon_path
    shortcut.save()
    print("Shortcut created successfully.")

if __name__ == "__main__":
    exe_path = os.path.abspath("dist/QR_full_app.exe")  # replace with your actual path
    print(f"EXE path: {exe_path}")
    icon_path = r"C:/Users/COMPUMARTS/OneDrive/Desktop/Python Projects/QR Generator App/app_icon.ico"  # 👈 Use your icon path
    create_shortcut(exe_path, "QR Generator", icon_path)

#  For desktop shortcut
# #  here Ai also helped me for making a desktop shortcut.
