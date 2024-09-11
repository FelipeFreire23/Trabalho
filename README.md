
# Sistema de Gerenciamento de Cadastros

Este é um projeto desenvolvido em Python utilizando o framework PyQt5 para a criação de uma interface gráfica de usuário (GUI). O sistema inclui funcionalidades para cadastro, pesquisa de pessoas, geração de relatórios e uma tela de bloqueio para controle de acesso.

## Funcionalidades

- **Tela de Bloqueio**: Controle de acesso inicial com autenticação de usuário e senha.
- **Cadastro**: Tela para inserção de novos cadastros com informações pessoais, incluindo foto.
- **Pesquisa**: Pesquisa de pessoas por nome ou telefone no banco de dados.
- **Relatórios**: Geração de relatórios em HTML e opção de exportar para DOCX.

## Estrutura do Projeto

- **MainWindow**: Janela principal com abas para navegação entre Home, Cadastro, Relatórios e Pesquisa.
- **TelaBloqueio**: Tela inicial de bloqueio para autenticação do usuário.
- **Cadastro**: Permite adicionar novos cadastros no banco de dados SQLite.
- **PesquisaWindow**: Realiza pesquisa de cadastros no banco de dados.
- **Relatorio**: Gera relatórios de cadastros existentes, com opção de salvar em DOCX.

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Instale as dependências:**

   Certifique-se de ter o Python 3 e o pip instalados. Para instalar as dependências, execute:

   ```bash
   pip install -r requirements.txt
   ```

   O arquivo `requirements.txt` deve incluir as seguintes bibliotecas:
   
   ```
   PyQt5
   python-docx
   ```

3. **Inicialize o Banco de Dados:**

   Antes de iniciar o aplicativo, certifique-se de que o banco de dados SQLite está configurado corretamente. Execute o script de criação de tabelas, se necessário.

4. **Execute o Aplicativo:**

   Para iniciar o sistema, execute:

   ```bash
   python main.py
   ```

## Uso

- **Tela de Bloqueio**: Ao iniciar o aplicativo, insira as credenciais (usuário: `admin`, senha: `admin`) para acessar a tela principal.
- **Home**: Página inicial do aplicativo.
- **Cadastro**: Clique na aba "Cadastro" e preencha os campos para adicionar um novo registro. É possível incluir uma foto do cadastro.
- **Relatórios**: Na aba "Relatórios", clique em "Gerar Relatório" para visualizar os dados e "Salvar como DOCX" para exportar.
- **Pesquisa**: Utilize a aba "Pesquisa" para buscar cadastros por nome ou telefone.

## Estrutura de Código

### Tela de Bloqueio (`TelaBloqueio`)

Esta classe implementa uma interface de bloqueio para garantir o acesso ao aplicativo apenas por usuários autorizados.

### Janela Principal (`MainWindow`)

A janela principal (`MainWindow`) organiza as diferentes funcionalidades em abas:

- **HomeWindow**: Exibe a página inicial.
- **Cadastro**: Fornece um formulário para adicionar novos cadastros ao banco de dados.
- **Relatórios**: Gera e exibe relatórios dos cadastros existentes.
- **Pesquisa**: Permite buscar registros específicos no banco de dados.

### Cadastro (`Cadastro`)

Implementa a lógica para inserção de novos cadastros, incluindo validações de campo e a possibilidade de adicionar uma foto ao cadastro.

### Pesquisa (`PesquisaWindow`)

Fornece uma interface para pesquisa de registros no banco de dados SQLite por nome ou telefone, com resultados exibidos na interface.

### Relatórios (`Relatorio`)

Responsável pela geração de relatórios detalhados dos cadastros existentes, exibindo-os na tela e permitindo a exportação para documentos DOCX.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).


