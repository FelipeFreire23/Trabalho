import sys
import re
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QDateEdit, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDate

# Lista de estados brasileiros
estados_brasileiros = [
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"
]

class CadastroDB:
    def conectar(self):
        return sqlite3.connect("cadastros.db")

    def criar_tabela(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS cadastro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_completo TEXT,
            data_nascimento TEXT,
            raca TEXT,
            escolaridade TEXT,
            genero TEXT,
            telefone TEXT,
            filhos TEXT,
            estado TEXT,
            municipio TEXT,
            foto BLOB  -- Adicionando coluna para foto como BLOB
        )''')
        conexao.commit()
        conexao.close()

    def inserir_dados(self, dados, foto=None):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute('''INSERT INTO cadastro (
            nome_completo, data_nascimento, raca, escolaridade, genero, telefone, filhos, estado, municipio, foto
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (
            dados["nome_completo"],
            dados["data_nascimento"],
            dados["raca"],
            dados["escolaridade"],
            dados["genero"],
            dados["telefone"],
            dados["filhos"],
            dados["estado"],
            dados["municipio"],
            foto
        ))
        conexao.commit()
        conexao.close()

    def carregar_foto(self, id):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute('SELECT foto FROM cadastro WHERE id = ?', (id,))
        foto = cursor.fetchone()[0]
        conexao.close()
        return foto

class Cadastro(QWidget):
    def __init__(self):
        super().__init__()
        self.db = CadastroDB()
        self.db.criar_tabela()  # Garantir que a tabela seja criada
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Cadastro")
        self.setGeometry(100, 100, 700, 500)
        self.setStyleSheet("background-color: #F0E68C;")

        # Layout principal
        layout = QVBoxLayout()

        # Título
        self.titulo = QLabel("Cadastro", self)
        self.titulo.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(self.titulo)

        # Layout para os campos de entrada
        form_layout = QVBoxLayout()

        # Nome Completo
        self.label_nome = QLabel("Nome Completo", self)
        self.nome_completo = QLineEdit(self)
        form_layout.addWidget(self.label_nome)
        form_layout.addWidget(self.nome_completo)

        # Data de Nascimento
        self.label_data_nascimento = QLabel("Data de Nascimento", self)
        self.data_nascimento_entry = QDateEdit(self)
        self.data_nascimento_entry.setCalendarPopup(True)
        self.data_nascimento_entry.setDate(QDate.currentDate())
        form_layout.addWidget(self.label_data_nascimento)
        form_layout.addWidget(self.data_nascimento_entry)

        # Raça/Cor
        self.label_raca = QLabel("Raça/Cor", self)
        self.menu_raca = QComboBox(self)
        self.menu_raca.addItems(["Branca", "Preta", "Parda", "Amarela", "Indígena", "Outra"])
        form_layout.addWidget(self.label_raca)
        form_layout.addWidget(self.menu_raca)

        # Escolaridade
        self.label_escolaridade = QLabel("Escolaridade", self)
        self.menu_escolaridade = QComboBox(self)
        self.menu_escolaridade.addItems([
            "Ensino Fundamental", "Fundamental I (1º ao 5º ano) Incompleto",
            "Fundamental I (1º ao 5º ano) Completo", "Fundamental II (6º ao 9º ano) Incompleto",
            "Fundamental II (6º ao 9º ano) Completo", "Ensino Médio",
            "Ensino Médio Incompleto", "Ensino Médio Completo",
            "Ensino Médio Técnico Incompleto", "Ensino Médio Técnico Completo",
            "Ensino Superior", "Graduação (Bacharelado, Licenciatura, Tecnólogo) Incompleto",
            "Graduação (Bacharelado, Licenciatura, Tecnólogo) Completo",
            "Pós-Graduação (Especialização, MBA) Incompleto",
            "Pós-Graduação (Especialização, MBA) Completo",
            "Mestrado Incompleto", "Mestrado Completo", "Doutorado Incompleto",
            "Doutorado Completo", "Pós-Doutorado Incompleto", "Pós-Doutorado Completo"
        ])
        form_layout.addWidget(self.label_escolaridade)
        form_layout.addWidget(self.menu_escolaridade)

        # Gênero
        self.label_genero = QLabel("Gênero", self)
        self.menu_genero = QComboBox(self)
        self.menu_genero.addItems(["Heterossexual", "Homossexual", "Bissexual", "Assexual", "Pansexual", "Demissexual"])
        form_layout.addWidget(self.label_genero)
        form_layout.addWidget(self.menu_genero)

        # Telefone
        self.label_telefone = QLabel("Telefone", self)
        self.telefone = QLineEdit(self)
        self.telefone.textChanged.connect(self.formatar_telefone)
        form_layout.addWidget(self.label_telefone)
        form_layout.addWidget(self.telefone)

        # Têm filhos?
        self.label_filhos = QLabel("Têm filhos?", self)
        self.menu_filhos = QComboBox(self)
        self.menu_filhos.addItems(["Não", "Sim, 1", "Sim, 2", "Sim, 3", "Sim, 4 ou mais"])
        form_layout.addWidget(self.label_filhos)
        form_layout.addWidget(self.menu_filhos)

        # Estado
        self.label_estado = QLabel("Estado", self)
        self.menu_estado = QComboBox(self)
        self.menu_estado.addItems(estados_brasileiros)
        form_layout.addWidget(self.label_estado)
        form_layout.addWidget(self.menu_estado)

        # Município
        self.label_municipio = QLabel("Município", self)
        self.municipio = QLineEdit(self)
        form_layout.addWidget(self.label_municipio)
        form_layout.addWidget(self.municipio)

        # Layout para foto e seleção de arquivo
        foto_layout = QVBoxLayout()

        # Moldura para foto
        self.moldura_foto = QLabel(self)
        self.moldura_foto.setFixedSize(150, 200)
        self.moldura_foto.setStyleSheet("background-color: white; border: 1px solid black;")
        foto_layout.addWidget(self.moldura_foto)

        # Botão para selecionar foto
        self.botao_foto = QPushButton("Selecionar Foto", self)
        self.botao_foto.clicked.connect(self.selecionar_foto)
        foto_layout.addWidget(self.botao_foto)

        # Layout para o botão de envio
        self.botao_enviar = QPushButton("Salvar", self)
        self.botao_enviar.clicked.connect(self.enviar_dados)
        form_layout.addWidget(self.botao_enviar)

        # Layout horizontal para form_layout e foto_layout
        main_layout = QHBoxLayout()
        main_layout.addLayout(form_layout, 70)
        main_layout.addLayout(foto_layout, 30)

        layout.addLayout(main_layout)
        self.setLayout(layout)

    def formatar_telefone(self):
        telefone = self.telefone.text()
        telefone = re.sub(r'\D', '', telefone)
        if len(telefone) == 11:
            telefone_formatado = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
        elif len(telefone) == 10:
            telefone_formatado = f"({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}"
        else:
            telefone_formatado = telefone
        self.telefone.setText(telefone_formatado)

    def selecionar_foto(self):
        options = QFileDialog.Options()
        arquivo_foto, _ = QFileDialog.getOpenFileName(self, "Selecionar Foto", "", "Imagens (*.png *.jpg *.jpeg)", options=options)
        if arquivo_foto:
            pixmap = QPixmap(arquivo_foto)
            pixmap = pixmap.scaled(self.moldura_foto.width(), self.moldura_foto.height())
            self.moldura_foto.setPixmap(pixmap)
            self.foto_path = arquivo_foto  # Armazenar o caminho da foto para uso posterior

    def enviar_dados(self):
        dados = {
            "nome_completo": self.nome_completo.text(),
            "data_nascimento": self.data_nascimento_entry.date().toString("dd/MM/yyyy"),
            "raca": self.menu_raca.currentText(),
            "escolaridade": self.menu_escolaridade.currentText(),
            "genero": self.menu_genero.currentText(),
            "telefone": self.telefone.text(),
            "filhos": self.menu_filhos.currentText(),
            "estado": self.menu_estado.currentText(),
            "municipio": self.municipio.text()
        }
        
        # Ler a foto como binário
        foto = None
        if hasattr(self, 'foto_path'):
            with open(self.foto_path, 'rb') as file:
                foto = file.read()
        
        # Inserir dados no banco de dados
        self.db.inserir_dados(dados, foto)
        QMessageBox.information(self, "Dados Salvos", "Dados salvos com sucesso!")

    def carregar_foto(self, id):
        foto = self.db.carregar_foto(id)
        if foto:
            with open("temp_foto.png", 'wb') as file:
                file.write(foto)
            pixmap = QPixmap("temp_foto.png")
            self.moldura_foto.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Cadastro()
    ex.show()
    sys.exit(app.exec_())
