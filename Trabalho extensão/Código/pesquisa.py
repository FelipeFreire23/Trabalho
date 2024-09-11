import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTextEdit, QMessageBox

class PesquisaWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pesquisa de Pessoa")
        self.setGeometry(100, 100, 400, 300)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label_telefone = QLabel("Telefone (xx)xxxxx-xxxx ou Nome:", self)
        self.busca = QLineEdit(self)
        layout.addWidget(self.label_telefone)
        layout.addWidget(self.busca)

        self.botao_pesquisar = QPushButton("Pesquisar", self)
        self.botao_pesquisar.clicked.connect(self.pesquisar_pessoa)
        layout.addWidget(self.botao_pesquisar)

        self.resultado = QTextEdit(self)
        self.resultado.setReadOnly(True)
        layout.addWidget(self.resultado)

        self.setLayout(layout)

    def pesquisar_pessoa(self):
        busca = self.busca.text()

        if busca:
            conexao = sqlite3.connect("cadastros.db")
            cursor = conexao.cursor()

            # Remove parênteses, traços e espaços da entrada de busca
            busca_limpa = busca.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")

            # Verifica se a busca parece um telefone (tem apenas números após a limpeza)
            if busca_limpa.isdigit():
                # Pesquisa por telefone, removendo parênteses e traços do telefone no banco também
                cursor.execute("""
                    SELECT * FROM cadastro 
                    WHERE REPLACE(REPLACE(REPLACE(REPLACE(telefone, '(', ''), ')', ''), '-', ''), ' ', '') = ?
                """, (busca_limpa,))
            else:
                # Pesquisa por nome (case insensitive)
                cursor.execute("SELECT * FROM cadastro WHERE nome_completo LIKE ?", ('%' + busca + '%',))

            dados = cursor.fetchone()
            conexao.close()

            if dados:
                # Ajuste os índices de acordo com a ordem das colunas na tabela
                id_pessoa = dados[0]         # Supondo que o ID seja a primeira coluna
                nome_pessoa = dados[1]       # Nome completo é a segunda coluna
                telefone_pessoa = dados[6]   # Telefone é a terceira coluna

                conteudo = f"ID: {id_pessoa}\nNome: {nome_pessoa}\nTelefone: {telefone_pessoa}"
                self.resultado.setText(conteudo)
            else:
                QMessageBox.warning(self, "Não Encontrado", "Nenhuma pessoa encontrada com essa pesquisa.")
        else:
            QMessageBox.warning(self, "Erro", "Preencha o campo de pesquisa.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PesquisaWindow()
    window.show()
    sys.exit(app.exec_())
