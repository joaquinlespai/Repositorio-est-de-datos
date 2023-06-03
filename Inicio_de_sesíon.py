import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMainWindow, \
    QPushButton, \
    QDialog, QDialogButtonBox, QMessageBox, QGridLayout
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QColor, QFont
from random import randint

class otherwindow(QWidget):
    def __init__(self):
        super().__init__()
        layer = QVBoxLayout()
        self.label0 = QLabel(f"NASHEX :{randint(5, 69)}")
        self.setWindowtTitle("ventana secundaria")
        layer.addWidget(self.label0)

        self.setLayout(layer)
class Miniwindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Miniwindow")
        self.setMinimumSize(200,200)
        layout = QVBoxLayout()

        # Etiquetas y campos de entrada para nombre de usuario y contraseña
        self.username_label = QLabel("Nombre de usuario:")
        self.username_input = QLineEdit()
        self.password_label = QLabel("Contraseña:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        # Botón de inicio de sesión
        self.login_button = QPushButton("Iniciar Sesión")
        self.login_button.clicked.connect(self.login)

        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Lógica de verificación de inicio de sesión aquí
        if username == "admin" and password == "password":
            print("Inicio de sesión exitoso")
        else:
            print("Credenciales incorrectas") 

class mywindow(QMainWindow):
    
    def setDarkMode(self, a0, amount=50):
        dark_mode = QColor(0 + amount, 0 + amount, 0 + amount)
        a0.setStyleSheet(f"background-color: {dark_mode.name()}; color: white")
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion de turismo")
        self.setMinimumSize(400, 400)

        self.button0 = QPushButton("logistica")
        self.button1 = QPushButton("Guia")
        self.button2 = QPushButton("Turista")
        self.button3 = QPushButton("cancelar")
        self.alt_window = Miniwindow()
        self.setDarkMode(self.alt_window)

        Main_box = QVBoxLayout()
        Box = QGridLayout()

        Box.addWidget(self.button0, 2, 0)
        Box.addWidget(self.button1, 2, 2)
        Box.addWidget(self.button2, 2, 3)
        Box.addWidget(self.button3, 6, 2)
        

        Main_box.addWidget(QLabel("Bienvenidos"))
        Main_box.addLayout(Box)
        Main_box.addWidget(self.button3)

        self.button0.clicked.connect(lambda checked: self.push_reaction(self.alt_window))
        self.button1.clicked.connect(lambda checked: self.push_reaction(self.alt_window))
        self.button2.clicked.connect(lambda checked: self.push_reaction(self.alt_window))
        self.button3.clicked.connect(lambda checked: self.cancelar)

        my_window = QWidget()
        my_window.setLayout(Main_box)
        self.setDarkMode(my_window)
        self.setCentralWidget(my_window)

    def cancelar(self):
        pass

    def push_reaction(self, window: Miniwindow):
        if window.isVisible():
            window.hide()
        else:
            window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mywindow()
    window.show()  # Obligatorio (dentro del init o fuera)
    app.exec()

