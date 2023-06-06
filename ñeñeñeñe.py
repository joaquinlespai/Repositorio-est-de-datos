import sys
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QLabel, QVBoxLayout, QWidget


class CalendarWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calendario de Turnos")
        self.setGeometry(100, 100, 400, 300)

        self.calendar = QCalendarWidget(self)
        self.calendar.clicked.connect(self.date_selected)

        self.date_label = QLabel(self)
        self.date_label.setText("Fecha seleccionada: ")

        self.turn_label = QLabel(self)
        self.turn_label.setText("Turno seleccionado: ")

        layout = QVBoxLayout()
        layout.addWidget(self.calendar)
        layout.addWidget(self.date_label)
        layout.addWidget(self.turn_label)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def date_selected(self, date):
        self.date_label.setText("Fecha seleccionada: " + date.toString('yyyy-MM-dd'))

        dialog = TurnSelectionDialog(self)
        if dialog.exec() == QDialog.Accepted:
            selected_turn = dialog.get_selected_turn()
            self.turn_label.setText("Turno seleccionado: " + selected_turn)


class TurnSelectionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Seleccionar Turno")

        layout = QVBoxLayout()

        morning_button = QPushButton("Mañana")
        morning_button.clicked.connect(self.select_morning)

        afternoon_button = QPushButton("Tarde")
        afternoon_button.clicked.connect(self.select_afternoon)

        evening_button = QPushButton("Noche")
        evening_button.clicked.connect(self.select_evening)

        layout.addWidget(morning_button)
        layout.addWidget(afternoon_button)
        layout.addWidget(evening_button)

        self.setLayout(layout)

        self.selected_turn = None

    def select_morning(self):
        self.selected_turn = "Mañana"
        self.accept()

    def select_afternoon(self):
        self.selected_turn = "Tarde"
        self.accept()

    def select_evening(self):
        self.selected_turn = "Noche"
        self.accept()

    def get_selected_turn(self):
        return self.selected_turn


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalendarWindow()
    window.show()
    sys.exit(app.exec())
