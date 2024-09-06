import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QDesktopWidget, QVBoxLayout, QPushButton, QHBoxLayout

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Layout Example")

layout = QHBoxLayout()
layout.addWidget(QLabel("this is label"))
layout.addWidget(QPushButton("this is button"))

window.setLayout(layout)

window.show()
sys.exit(app.exec_())
