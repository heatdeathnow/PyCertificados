from PySide6.QtWidgets import QMainWindow
from multiprocessing import Manager
from ui_form import Ui_MainWindow
from sys import exit
import var


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    var.manager = Manager()
    var.shared_list = var.manager.list(range(var.max_processes))
    var.lock = var.manager.Lock()

    widget = MainWindow()
    widget.setWindowTitle('Emissor de certificados')
    widget.show()

    exit(var.app.exec())
