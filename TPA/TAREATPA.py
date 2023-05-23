import re
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QMessageBox

class EmailValidator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Validador de correo electrónico')
        self.setGeometry(100, 100, 300, 150)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.email_edit = QLineEdit()
        self.email_edit.setPlaceholderText('Ingrese su correo electrónico')
        layout.addWidget(self.email_edit)

        self.validar_button = QPushButton('Validar')
        self.validar_button.clicked.connect(self.validar_correo)
        layout.addWidget(self.validar_button)

    def validar_correo(self):
        correo = self.email_edit.text()
        if not correo:
            QMessageBox.warning(self, 'Error', 'Por favor ingrese su correo electrónico.')
            return

        es_valido = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', correo)

        if es_valido:
            QMessageBox.information(self, 'Resultado', 'El correo electrónico es válido.')
        else:
            QMessageBox.warning(self, 'Resultado', 'El correo electrónico no es válido.')

if __name__ == '__main__':
    app = QApplication([])
    window = EmailValidator()
    window.show()
    app.exec()