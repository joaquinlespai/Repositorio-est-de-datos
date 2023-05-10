import sys

from PyQt6.QtWidgets import QApplication , QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMainWindow, \
    QPushButton, \
    QDialog, QDialogButtonBox, QMessageBox, QGridLayout
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QColor, QFont
from random import randint

class otherWindow(QWidget):
    def __init__(self):
        super().__init__()
        layer = QVBoxLayout()
        self.label0 = QLabel(f"increible : {randint(5 ,69)}")
        self.setWindowTitle("ventana secundaria")
        layer.addWidget(self.label0)

        self.setLayout(layer)

class Mywindow(QMainWindow):
    def setdarkmode(self, a0, amount=50):
        dark_mode = QColor(0 + amount, 0 + amount, 0+ amount)
        a0.setStyleSheet(f"background-color: {dark_mode.name()}; color: white")


class Mywindow(QDialog):
    def __init__(self):
        super().__init__()

        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        self.button = QDialogButtonBox(QBtn)
        self.button.accepted.connect(self.accept)
        self.button.rejected.connect(self.reject)
        self.main_layout = QVBoxLayout()
        self.layout = QGridLayout()
        self.entry1 = QLineEdit("")
        self.entry2 = QLineEdit("")
        self.entry3 = QLineEdit("")
        self.entry4 = QLineEdit("")
        self.entry5 = QLineEdit("")
        self.entry6 = QLineEdit("")
        self.layout.addWidget(QLabel("Atributo 1"), 1, 0)
        self.layout.addWidget(QLabel("Atributo 2"), 2, 0)
        self.layout.addWidget(QLabel("Atributo 3"), 3, 0)
        self.layout.addWidget(QLabel("Atributo 4"), 4, 0)
        self.layout.addWidget(QLabel("atributo 5"), 5, 0)
        self.layout.addWidget(QLabel("atributo 6"), 6, 0)
        self.layout.addWidget(self.entry1, 1, 1)
        self.layout.addWidget(self.entry2, 2, 1)
        self.layout.addWidget(self.entry3, 3, 1)
        self.layout.addWidget(self.entry4, 4, 1)
        self.layout.addWidget(self.entry5, 5, 1)
        self.layout.addWidget(self.entry6, 6, 1)
        self.setLayout(self.main_layout)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Prueba")
        self.setMinimumSize(400 , 500)
        self.button2 = QPushButton("cancel")

        main_box = QVBoxLayout()
        box = QGridLayout()

        main_box.addWidget(QLabel("Nombre de usuario"))
        main_box.addLayout(box)
        main_box.addWidget(self.button2)
        self.button2.clicked.connect(lambda checked: self.compare)

        My_window = QWidget()
        My_window.setLayout(main_box)
        self.setdarkmode(My_window)
        self.setCentralWidget(My_window)
    
    def compare(self):
        pass
    
    def push_reaction(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mywindow()
    window.show()  # Obligatorio (dentro del init o fuera)
    app.exec()