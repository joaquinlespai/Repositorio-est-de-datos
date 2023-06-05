class Selection(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Selecciona el tipo de senderismo que realizaras")

        layout = QVBoxLayout()

        self.label = QLabel("selecciona el senderismo a realizar:", self)
        layout.addWidget(self.label)

        self.btn_light = QPushButton("Senderismo light", self)
        self.btn_light.clicked.connect(self.selection_light)
        layout.addWidget(self.btn_light)

        self.btn_plus = QPushButton("senderismo plus", self)
        self.btn_plus.clicked.connect(self.selection_plus)
        layout.addWidget(self.btn_plus)

        self.btn_heavy = QPushButton("Senderismo heavy", self)
        self.btn_heavy.clicked.connect(self.selection_heavy)
        layout.addWidget(self.btn_heavy)

        self.setLayout(layout)

    def selection_light(self):
            self.accepted_type = "selection light"
            self.accept()

    def selection_plus(self):
            self.accepted_type = "selection_plus"
            self.accept()
    def selection_heavy(self):
            self.accepted_type = "selection_heavy"
            self.accept()