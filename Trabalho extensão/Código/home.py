class HomeWindow(QWidget):
    def __init__(self):
        super(HomeWindow, self).__init__()
        self.setWindowTitle("Home")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #FFFFFF;")
        layout = QVBoxLayout()
        self.label_home = QLabel("Bem-vindo à tela inicial!", self)
        layout.addWidget(self.label_home)
        self.setLayout(layout)