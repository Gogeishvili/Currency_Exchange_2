from PyQt5.QtWidgets import QMessageBox


class ErrorHandler(QMessageBox):
    def __init__(self, title, message):
        super().__init__()
        self.setIcon(QMessageBox.Warning)
        self.setWindowTitle(title)
        self.setText(message)
        self.exec_()
