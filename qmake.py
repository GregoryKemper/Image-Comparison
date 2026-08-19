import os
import sys
import subprocess

uic = os.path.join(os.path.dirname(sys.executable), "PySide6-uic.exe")

def run_qmake():
    ui_file = os.path.join("src", "mainGUILayout.ui")
    out_file = os.path.join("gen", "Ui_MainWindow.py")

    os.makedirs("gen", exist_ok=True)
    subprocess.run([uic, ui_file, "-o", out_file], check=True)


if __name__ == "__main__":
    run_qmake()