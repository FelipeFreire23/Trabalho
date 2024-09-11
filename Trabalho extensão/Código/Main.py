import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QWidget, QTabWidget
from Cadastro import Cadastro  # Importando a classe Cadastro
from Relatório import Relatorio  # Importando a classe Relatorio
from pesquisa import PesquisaWindow  # Importando a classe PesquisaWindow do arquivo Pesquisa.py

class TelaBloqueio(QDialog):
    def __init__(self, main_window):
        super(TelaBloqueio, self).__init__()
        self.main_window = main_window
        self.setWindowTitle("Tela de Bloqueio")
        self.setGeometry(100, 100, 300, 200)
        self.setStyleSheet("background-color: #F0E68C;")

        layout = QVBoxLayout()

        # Rótulo e campo de entrada para usuário
        self.label_usuario = QLabel("Usuário:", self)
        self.label_usuario.setStyleSheet("background-color: #F0E68C;")
        layout.addWidget(self.label_usuario)

        self.usuario_entry = QLineEdit(self)
        layout.addWidget(self.usuario_entry)

        # Rótulo e campo de entrada para senha
        self.label_senha = QLabel("Senha:", self)
        self.label_senha.setStyleSheet("background-color: #F0E68C;")
        layout.addWidget(self.label_senha)

        self.senha_entry = QLineEdit(self)
        self.senha_entry.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.senha_entry)

        # Botão para desbloquear
        self.botao_desbloquear = QPushButton("Desbloquear", self)
        self.botao_desbloquear.clicked.connect(self.desbloquear)
        layout.addWidget(self.botao_desbloquear)

        self.setLayout(layout)

        # Usuário padrão
        self.usuario_senha = {"admin": "admin"}

    def desbloquear(self):
        usuario = self.usuario_entry.text()
        senha = self.senha_entry.text()
        if usuario in self.usuario_senha and self.usuario_senha[usuario] == senha:
            self.accept()  # Fecha a janela de diálogo e retorna 1
            self.main_window.show()  # Mostra a janela principal novamente
        else:
            QMessageBox.critical(self, "Erro", "Usuário ou senha incorretos!")

class HomeWindow(QWidget):
    def __init__(self):
        super(HomeWindow, self).__init__()
        self.setWindowTitle("Home")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #FFFFFF;")
        layout = QVBoxLayout()
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Aplicativo Principal")
        
        # Ajustar tamanho da janela
        self.setGeometry(300, 100, 800, 600)  # Largura de 800 e altura de 600
        
        # Definindo cor de fundo cinza e transparência
        self.setStyleSheet("QMainWindow { background-color: rgba(128, 128, 128, 180); }")  # Cinza com transparência
        
        # Criando um widget central e definindo como central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Layout principal
        layout = QVBoxLayout()
        
        # Criação do QTabWidget
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        # Criando as abas
        self.tab_home = HomeWindow()
        self.tab_cadastro = QWidget()
        self.tab_relatorios = QWidget()
        self.tab_pesquisa = QWidget()

        # Configurando o layout para cada aba
        cadastro_layout = QVBoxLayout()
        relatorios_layout = QVBoxLayout()
        pesquisa_layout = QVBoxLayout()

        # Adicionando botões às abas
        self.botao_cadastro = QPushButton("Abrir Cadastro")
        self.botao_cadastro.clicked.connect(self.abrir_cadastro)
        cadastro_layout.addWidget(self.botao_cadastro)
        self.tab_cadastro.setLayout(cadastro_layout)

        self.botao_relatorios = QPushButton("Relatórios")
        self.botao_relatorios.clicked.connect(self.abrir_relatorios)
        relatorios_layout.addWidget(self.botao_relatorios)
        self.tab_relatorios.setLayout(relatorios_layout)

        self.botao_pesquisar = QPushButton("Pesquisar")
        self.botao_pesquisar.clicked.connect(self.abrir_pesquisa)
        pesquisa_layout.addWidget(self.botao_pesquisar)
        self.tab_pesquisa.setLayout(pesquisa_layout)

        # Adicionando as abas ao QTabWidget
        self.tab_widget.addTab(self.tab_home, "Home")
        self.tab_widget.addTab(self.tab_cadastro, "Cadastro")
        self.tab_widget.addTab(self.tab_relatorios, "Relatórios")
        self.tab_widget.addTab(self.tab_pesquisa, "Pesquisa")

    def abrir_cadastro(self):
        self.cadastro_window = Cadastro()
        self.cadastro_window.show()

    def abrir_relatorios(self):
        self.relatorio_window = Relatorio()
        self.relatorio_window.show()

    def abrir_pesquisa(self):
        self.pesquisa_window = PesquisaWindow()
        self.pesquisa_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()

    # Criação da tela de bloqueio
    tela_bloqueio = TelaBloqueio(main_window)
    if tela_bloqueio.exec_() == QDialog.Accepted:
        sys.exit(app.exec_())
