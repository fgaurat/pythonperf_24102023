from main_window import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
if __name__ == '__main__':
    main()
