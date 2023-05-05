from PySide6.QtWidgets import QApplication, QWidget
from ui_form import Ui_Widget
from sys import argv, exit
from multiprocessing import Manager
import var


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)


if __name__ == "__main__":
    var.manager = Manager()
    var.shared_list = var.manager.list(range(var.max_processes))
    var.lock = var.manager.Lock()

    app = QApplication(argv)

    widget = Widget()
    widget.setWindowTitle('Emissor de certificados')
    widget.show()
    exit(app.exec())
