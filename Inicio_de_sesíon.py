import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMainWindow, \
    QPushButton, \
    QDialog, QDialogButtonBox, QMessageBox, QGridLayout
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QColor, QFont
from random import randint

class guiasventana(QWidget):
    def __init__(self, availability, excursion_type):
        super().__init__()
        layer = QVBoxLayout()
        self.label0 = QLabel(f"Días :{randint(2, 7)}")
        self.setWindowTitle("Ventana de Guias")
        self.setMinimumSize(100,250)
        layer.addWidget(self.label0)
        layer.addWidget(QLabel(f"Disponibilidad: {availability} días"))
        layer.addWidget(QLabel(f"Tipo de excursión: {excursion_type}"))
        layer.addWidget(self.label0)
        self.setLayout(layer)
class logisticaventana(QWidget):
    def __init__(self):
        super().__init__()
        layer = QVBoxLayout()
        self.label1 = QLabel(f"hola que tal")
        self.setWindowTitle("Ventana para losgitica")
        self.setMinimumSize(250,250)
        layer.addWidget(self.label1)
        layer.addWidget(QLabel((f"sexoooo")))
        layer.addWidget(QLabel((f"sexooooo2")))
        layer.addWidget(self.label1)
        self.setLayout(layer)

class turistasventana(QWidget):
    def __init__(self):
        super().__init__()
        layer = QVBoxLayout()
        self.label2 = QLabel(f"turista puto")
        self.setWindowTitle("Ventana para turistas")
        self.setMinimumSize(250,250)
        layer.addWidget(self.label2)
        layer.addWidget(QLabel((f"turismo")))
        layer.addWidget(QLabel((f"excursiones")))
        layer.addWidget(self.label2)
        self.setLayout(layer)

class Miniwindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Miniwindow")
        self.setMinimumSize(400,200)
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
        self.cancel_button = QPushButton("Cancelar")
        self.cancel_button.clicked.connect(self.close)

        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.cancel_button)

        self.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Lógica de verificación de inicio de sesión aquí
        if username == "guias" and password == "excursiones":
            print("Inicio de sesión exitoso")
            self.close()
            availability = randint(2, 5)
            excursion_type = ("heavy")
            self.other_window = guiasventana(availability, excursion_type)
            self.other_window.show()

        elif username == "logistica" and password == "materiales":
            print("Inicio de sesión exitoso")
            self.close()
            self.other_window = logisticaventana()
            self.other_window.show()

        elif username == "turista" and password == "turismo":
            print("Inicio de sesión exitoso")
            self.close()
            self.other_window = turistasventana()
            self.other_window.show()
        else:
            print("Inicio de sesión fallido")  

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
        self.button3.clicked.connect(self.cancelar)

        my_window = QWidget()
        my_window.setLayout(Main_box)
        self.setDarkMode(my_window)
        self.setCentralWidget(my_window)

    def cancelar(self):
        self.close()

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