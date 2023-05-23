import sys

from PyQt6.QtWidgets import QApplication , QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMainWindow, \
    QPushButton, \
    QDialog, QDialogButtonBox, QMessageBox, QGridLayout
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QColor, QFont
from random import randint


from VentanaPrincipal import Ui_VentanaPrincipal

class Mywindow(QMainWindow):
    def setdarkmode(self, a0, amount=50):
        dark_mode = QColor(0 + amount, 0 + amount, 0+ amount)
        a0.setStyleSheet(f"background-color: {dark_mode.name()}; color: white")

class Mascota:
    def __init__(self, nombre: str, especie: str, edad: int, peso:float):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

    def __str__(self) -> str:
        return f"Mascota {self.nombre} de {self.edad} anios de la especie {self.especie} con {self.peso} Kg."


class Ventana(QtWidgets.QMainWindow, Ui_VentanaPrincipal):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ventana, self).__init__(*args, **kwargs)
        #Implementación de Ui_VentanaPrincipal
        self.setupUi(self)
        self.obj = obj
        self.pushButton.clicked.connect(self.guardar_mascota)

    def guardar_mascota(self):
        print(self.obj.nombre)

        self.obj.nombre = self.entrada_nombre.text()
        self.obj.especie = self.entrada_especie.text()
        self.obj.edad = self.entrada_edad.text()
        self.obj.peso = self.entrada_peso.text()

        self.entrada_nombre.setText("")
        self.entrada_especie.setText("")
        self.entrada_edad.setValue(0)
        self.entrada_peso.setValue(0)

        print(self.obj.nombre)
        print(self.obj.especie)
        print(self.obj.edad)
        print(self.obj.peso)
        vista = Ventana(obj=Mascota("", "", 0, 0))
        
    
    def guardar_mascota(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    vista = Ventana()
    vista.show()
    app.exec()