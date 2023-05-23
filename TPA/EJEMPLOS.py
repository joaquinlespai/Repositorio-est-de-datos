import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMainWindow, \
    QPushButton, \
    QDialog, QDialogButtonBox, QMessageBox, QGridLayout
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QColor, QFont
from random import randint


class otherWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(200, 100)
        layer = QVBoxLayout()
        self.label0 = QLabel("error")
        self.button = QPushButton("HeHe")
        self.entry = QLineEdit("")
        self.setWindowTitle(" ")
        layer.addWidget(self.label0)
        layer.addWidget(self.entry)
        layer.addWidget(self.button)

        self.setLayout(layer)


class myWindow(QMainWindow):

    def setDarkMode(self, a0, amount=50):
        dark_mode = QColor(0 + amount, 0 + amount, 0 + amount)
        a0.setStyleSheet(f"background-color: {dark_mode.name()}; color: white")

    def __init__(self):
        super().__init__()

        # Sección de ventana y configuración general
        self.setWindowTitle("HeHe")
        self.setMinimumSize(400, 200)

        # Constructor
        self.button = QPushButton("HeHe")
        self.label = QLabel("HeHe")
        self.alt_window = otherWindow()
        self.setDarkMode(self.alt_window)

        # Layout y reacción
        box = QVBoxLayout()
        box1 = QGridLayout()
        box2 = QVBoxLayout()
        self.button.clicked.connect(lambda checked: self.push_reaction(self.alt_window))

        box.addWidget(self.label)
        box.addWidget(self.button)

        my_window = QWidget()
        my_window.setLayout(box)
        self.setDarkMode(my_window)
        self.setDarkMode(self.button, 70)
        self.setCentralWidget(my_window)

    def push_reaction(self, window: otherWindow):
        """
        if self.alt_window is None:
            self.alt_window = otherWindow()
            self.alt_window.show()  # Permite desplegar la ventana en la pantalla
        else:
            self.alt_window.close()
            self.alt_window = None
        """
        window.label0.setText("Nombre:")

        if window.isVisible():
            window.hide()
        else:
            window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = myWindow()
    window.show()  # Obligatorio (dentro del init o fuera)
    app.exec()