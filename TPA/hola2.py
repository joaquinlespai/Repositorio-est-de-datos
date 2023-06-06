from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QPushButton, QLabel

class SenderismoDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Selección de Senderismo")

        layout = QVBoxLayout()

        self.label = QLabel("Seleccione un tipo de senderismo:", self)
        layout.addWidget(self.label)

        self.btn_light = QPushButton("Senderismo Light", self)
        self.btn_light.clicked.connect(self.select_light)
        layout.addWidget(self.btn_light)

        self.btn_plus = QPushButton("Senderismo Plus", self)
        self.btn_plus.clicked.connect(self.select_plus)
        layout.addWidget(self.btn_plus)

        self.btn_heavy = QPushButton("Senderismo Heavy", self)
        self.btn_heavy.clicked.connect(self.select_heavy)
        layout.addWidget(self.btn_heavy)

        self.setLayout(layout)

    def select_light(self):
        self.accepted_type = "Senderismo Light"
        self.accept()

    def select_plus(self):
        self.accepted_type = "Senderismo Plus"
        self.accept()

    def select_heavy(self):
        self.accepted_type = "Senderismo Heavy"
        self.accept()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Agencia de Turismo CTCh")
        self.setGeometry(100, 100, 400, 300)

        self.btn_select_senderismo = QPushButton("Seleccionar Tipo de Senderismo", self)
        self.btn_select_senderismo.clicked.connect(self.open_senderismo_dialog)
        self.setCentralWidget(self.btn_select_senderismo)

    def open_senderismo_dialog(self):
        dialog = SenderismoDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            selected_type = dialog.accepted_type
            self.show_message(f"Tipo de senderismo seleccionado: {selected_type}")

    def show_message(self, message):
        QMessageBox.information(self, "Mensaje", message)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
