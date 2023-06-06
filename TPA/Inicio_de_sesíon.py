import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMainWindow, \
    QPushButton, \
    QDialog, QDialogButtonBox, QMessageBox, QGridLayout
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QColor, QFont
from random import randint

class guiasventana(QWidget):
    
    def setDarkMode(self, a0, amount=50):
        dark_mode = QColor(0 + amount, 0 + amount, 0 + amount)
        a0.setStyleSheet(f"background-color: {dark_mode.name()}; color: white")
    
    def __init__(self, availability, excursion_type):
        super().__init__()
        layer = QVBoxLayout()
        self.label0 = QLabel(f"Días de descanso: tienes de por si 2 días de descansa, dias extras disponibles {randint(0, 2)}")
        self.setWindowTitle("Ventana de Guias")
        self.setMinimumSize(100,250)
        layer.addWidget(self.label0)
        layer.addWidget(QLabel(f"Disponibilidad: {availability}"))
        layer.addWidget(QLabel(f"Tipo de excursión: {excursion_type}"))
        layer.addWidget(self.label0)
        self.setLayout(layer)
    
def get_disponibilidad():
    disponibilidad = random.choice(["si disponible", "no disponible"])
    return disponibilidad

class logisticaventana(QWidget):
    
    def setDarkMode(self, a0, amount=50):
        dark_mode = QColor(0 + amount, 0 + amount, 0 + amount)
        a0.setStyleSheet(f"background-color: {dark_mode.name()}; color: white")
    
    def __init__(self, avalability2):
        super().__init__()
        layer = QVBoxLayout()
        self.label1 = QLabel(f"Transporte")
        self.setWindowTitle("Ventana para losgitica")
        self.setMinimumSize(250,250)
        layer.addWidget(self.label1)
        layer.addWidget(QLabel(f"Alojamiento :{avalability2}"))
        layer.addWidget(QLabel((f"Pasajes")))
        layer.addWidget(self.label1)
        self.setLayout(layer)
def get_disponibilidad2():
    disponibilidad = random.choice(["si se encuentra con disponibbles", "no disponible"])
    return disponibilidad
class turistasventana(QWidget):
    
    def setDarkMode(self, a0, amount=50):
        dark_mode = QColor(0 + amount, 0 + amount, 0 + amount)
        a0.setStyleSheet(f"background-color: {dark_mode.name()}; color: white")
    
    def __init__(self, excursion_turista):
        super().__init__()
        layer = QVBoxLayout()
        self.label2 = QLabel(f"Guias acompañastes: 1 obligatorio ")
        self.setWindowTitle("Ventana para turistas")
        self.setMinimumSize(250,250)
        layer.addWidget(self.label2)
        layer.addWidget(QLabel(f"plan elegido: {excursion_turista}"))
        layer.addWidget(QLabel(f"Guias necesarios: {randint(0, 2)}"))
        layer.addWidget(self.label2)
        self.setLayout(layer)

class Selection(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Selecciona el tipo de senderismo que realizarás")

        layout = QVBoxLayout()

        self.label = QLabel("Selecciona el senderismo a realizar:", self)
        layout.addWidget(self.label)

        self.btn_light = QPushButton("Senderismo light", self)
        self.btn_light.clicked.connect(self.selection_light)
        layout.addWidget(self.btn_light)

        self.btn_plus = QPushButton("Senderismo plus", self)
        self.btn_plus.clicked.connect(self.selection_plus)
        layout.addWidget(self.btn_plus)

        self.btn_heavy = QPushButton("Senderismo heavy", self)
        self.btn_heavy.clicked.connect(self.selection_heavy)
        layout.addWidget(self.btn_heavy)

        self.setLayout(layout)

    def selection_light(self):
        self.accepted_type = "senderismo light"
        self.accept()

    def selection_plus(self):
        self.accepted_type = "senderismo plus"
        self.accept()

    def selection_heavy(self):
        self.accepted_type = "senderismo heavy"
        self.accept()

class Turistasexcursion(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Selecciona el tipo de senderismo que realizarás")

        layout = QVBoxLayout()

        self.label = QLabel("Selecciona el senderismo a realizar:", self)
        layout.addWidget(self.label)

        self.btn_light = QPushButton("Senderismo light", self)
        self.btn_light.clicked.connect(self.selection_light)
        layout.addWidget(self.btn_light)

        self.btn_plus = QPushButton("Senderismo plus", self)
        self.btn_plus.clicked.connect(self.selection_plus)
        layout.addWidget(self.btn_plus)

        self.btn_heavy = QPushButton("Senderismo heavy", self)
        self.btn_heavy.clicked.connect(self.selection_heavy)
        layout.addWidget(self.btn_heavy)

        self.setLayout(layout)

    def selection_light(self):
        self.accepted_type = "senderismo light"
        self.accept()

    def selection_plus(self):
        self.accepted_type = "senderismo plus"
        self.accept()

    def selection_heavy(self):
        self.accepted_type = "senderismo heavy"
        self.accept()
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
            availability = get_disponibilidad()
            excursion_type_dialog = Selection()
            if excursion_type_dialog.exec() == QDialog.DialogCode.Accepted:
                excursion_type = excursion_type_dialog.accepted_type
                self.other_window = guiasventana(availability, excursion_type)
                self.other_window.show()

        elif username == "logistica" and password == "materiales":
            print("Inicio de sesión exitoso")
            self.close()
            availability2 = get_disponibilidad2()
            self.other_window = logisticaventana(availability2)
            self.other_window.show()

        elif username == "turista" and password == "turismo":
            print("Inicio de sesión exitoso")
            self.close()
            excursion_type_dialog = Turistasexcursion()
            if excursion_type_dialog.exec() == QDialog.DialogCode.Accepted:
                excursion_type = excursion_type_dialog.accepted_type
                self.other_window = turistasventana(excursion_type)
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