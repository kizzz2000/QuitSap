import pygetwindow as gw
import pyautogui
import sys
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
import psutil

ui_file_name = "quit.ui"
ui_file = QFile(ui_file_name)
if not ui_file.open(QIODevice.ReadOnly):
    print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
    sys.exit(-1)
loader = QUiLoader()
ui_file.close()

class App(QApplication):
    def __init__(self):
        super().__init__()
        self.ui = loader.load(ui_file)
#               Button name                 function  #
        self.ui.startsapgui.clicked.connect(self.open_sap_gui)
        self.ui.quitsapgui.clicked.connect(self.close_sap_gui)
        self.ui.startautoclicker.clicked.connect(self.start_auto_clicker)
        self.ui.quitautoclicker.clicked.connect(self.stop_auto_clicker)
        self.ui.show()

    def open_sap_gui(self):
        handle = gw.getWindowsWithTitle('AutoJob2.0')[0]
        handle.activate()
        pyautogui.hotkey("shift", "f10")

    def kill_process(self, process_name):
        processes = filter(lambda p: p.name() == 'python.exe', psutil.process_iter())
        for process in processes:
            if process_name in psutil.Process(process.pid).exe():
                process.kill()
                break


    def close_sap_gui(self):
        self.kill_process("AutoJob2.0")


    def start_auto_clicker(self):
        handle = gw.getWindowsWithTitle('AutoClicker – main.py')[0]
        handle.activate()
        pyautogui.hotkey("shift", "f10")

    def stop_auto_clicker(self):
        handle = gw.getWindowsWithTitle('AutoClicker – main.py')[0]
        handle.activate()
        pyautogui.hotkey("ctrl", "f2")

if __name__ == "__main__":
    app = App()
    sys.exit(app.exec())