from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPushButton

class Selection(QDialog):
    def __init__(self, parent=None):
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
        self.accepted_type = "Senderismo light"
        self.accept()

    def selection_plus(self):
        self.accepted_type = "Senderismo plus"
        self.accept()

    def selection_heavy(self):
        self.accepted_type = "Senderismo heavy"
        self.accept()

# Crear una instancia de QApplication
app = QApplication([])

# Crear una instancia de la ventana de selección
selection_dialog = Selection()

# Mostrar la ventana de selección
selection_dialog.exec()

# Obtener el tipo de senderismo seleccionado
accepted_type = selection_dialog.accepted_type
print("Tipo de senderismo seleccionado:", accepted_type)
