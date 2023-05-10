
        box.addWidget(QLabel("Objeto izquierda:"), 0, 0)
        box.addWidget(self.atribute0, 1, 0)
        box.addWidget(self.button0, 2, 0)
        box.addWidget(QLabel("><"), 1, 1)
        box.addWidget(QLabel("Objecto derecha"), 0, 2)
        box.addWidget(self.atribute1, 1, 2)
        box.addWidget(self.button1, 2, 2)

        main_box.addWidget(QLabel("Bienvenidos"))
        main_box.addLayout(box)
        main_box.addWidget(self.button2)

        self.button0.clicked.connect(lambda checked: self.push_reaction(self.alt_window, 0))
        self.button1.clicked.connect(lambda checked: self.push_reaction(self.alt_window, 1))
        self.button2.clicked.connect(lambda checked: self.compare)

        my_window = QWidget()
        my_window.setLayout(main_box)
        self.setDarkMode(my_window)
        self.setCentralWidget(my_window)

    def myUpdate(self, aux: list):
        res = ""
        for i in aux:
            res += str(i) + ", "