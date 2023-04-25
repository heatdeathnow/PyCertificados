from PySide6.QtWidgets import QApplication, QWidget
from ui_form import Ui_Widget
from sys import argv, exit

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(argv)

    widget = Widget()
    widget.setWindowTitle('Emissor de certificados')
    widget.show()
    exit(app.exec())
