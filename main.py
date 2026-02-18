import sys
from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WaveSentrix Studio")
        self.resize(900, 600)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
