# Python Cadastro 2.0 🚀

[pt-br] | [en](#-english-version)

---

## 🇧🇷 Versão em Português

O **Python Cadastro 2.0** é uma aplicação modular desenvolvida em Python para gestão de cadastros, sanitização de dados, validação de entradas e armazenamento local em formato JSON.

O projeto conta com módulos organizados para tratamento de entrada de dados, validação de regras de negócio e estilização de terminal/interface. Além disso, o repositório inclui estrutura pronta para compilação executável com **PyInstaller**.

### 📌 Sumário
- [Funcionalidades](#-funcionalidades)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Pré-requisitos](#-pré-requisitos)
- [Como Executar](#-como-executar)
- [Descrição dos Módulos](#-descrição-dos-módulos)
- [Compilando com PyInstaller](#-compilando-com-pyinstaller)
- [Licença](#-licença)

### ✨ Funcionalidades
- **Tratamento de Dados:** Sanitização e formatação das entradas de utilizador em tempo real.
- **Validação de Dados:** Aplicação de regras de integridade para evitar entradas inválidas ou vazias.
- **Armazenamento JSON:** Persistência e leitura local de dados diretamente no ficheiro `armazenar.json`.
- **Estilização de Terminal:** Módulo de cores e modelos visuais centralizado para melhor experiência visual.
- **Navegação e Rotas:** Gestão de opções, rotas e fluxo de saída (checkout) do sistema.

### 📂 Estrutura do Projeto
```
Python Cadastro 2.0/
├── build/                 # Artefatos de compilação do PyInstaller
├── armazenar.json         # Ficheiro local de armazenamento de dados
├── chekout.py             # Lógica de finalização/checkout do sistema
├── conectar_json.py       # Manipulação de leitura e escrita do JSON
├── cores_modelos.py       # Definição de cores e estilos de terminal
├── destinos.py            # Gestão de opções e rotas
├── tratamento_input.py    # Sanitização e tratamento de inputs
├── verificacao_dados.py   # Validação das regras de negócio dos dados
└── .gitattributes         # Configurações do repositório Git
```

### 🛠️ Pré-requisitos
Certifique-se de ter o **Python 3.8+** instalado em sua máquina.

```bash
python --version
```

### 🚀 Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/python-cadastro-2.0.git
   cd python-cadastro-2.0
   ```

2. Execute o script principal:
   ```bash
   python chekout.py
   ```

### 🧩 Descrição dos Módulos
- **`conectar_json.py`**: Gerencia operações de leitura e gravação no `armazenar.json`.
- **`tratamento_input.py`**: Limpa e formata os dados fornecidos pelo utilizador.
- **`verificacao_dados.py`**: Verifica a integridade (e-mails, IDs, campos obrigatórios, etc.) antes da persistência.
- **`cores_modelos.py`**: Módulo de suporte para mensagens coloridas e layouts de terminal.
- **`destinos.py`**: Mapeia destinos e opções de navegação dentro da aplicação.
- **`chekout.py`**: Controla o fluxo de encerramento e consolidação do processo.

### 📦 Compilando com PyInstaller
Para gerar um executável (`.exe` ou binário local) a partir do código-fonte:

1. Instale o PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Gere o executável a partir do arquivo principal:
   ```bash
   pyinstaller --onefile chekout.py
   ```
Os ficheiros gerados estarão nas pastas `build/` e `dist/`.

---

## 🇺🇸 English Version

**Python Registration System 2.0** is a modular Python application designed for data registration, input sanitization, verification, and local JSON storage.

The project features dedicated modules for handling input formatting, business logic validation, and terminal UI styling. Furthermore, the repository includes pre-configured build assets ready for executable packaging using **PyInstaller**.

### 📌 Table of Contents
- [Features](#-features-1)
- [Project Structure](#-project-structure-1)
- [Prerequisites](#-prerequisites-1)
- [How to Run](#-how-to-run-1)
- [Module Breakdown](#-module-breakdown-1)
- [Building with PyInstaller](#-building-with-pyinstaller-1)
- [License](#-license-1)

### ✨ Features
- **Input Processing:** Real-time sanitization and formatting of user inputs.
- **Data Validation:** Strict rules to prevent typos, null fields, and logical inconsistencies.
- **JSON Storage:** Direct utility functions for reading and persisting data locally in `armazenar.json`.
- **Custom Styling:** Centralized color schemes and visual output formatting via dedicated modules.
- **Checkout & Routing:** Management of program navigation, user destinations, and exit flows.

### 📂 Project Structure
```
Python Cadastro 2.0/
├── build/                 # PyInstaller build artifacts
├── armazenar.json         # Local database in JSON format
├── chekout.py             # Checkout/completion flow logic
├── conectar_json.py       # JSON reading/writing handler
├── cores_modelos.py       # Terminal UI styles and color definitions
├── destinos.py            # Route and target management
├── tratamento_input.py    # Input sanitization utilities
├── verificacao_dados.py   # Data validation and integrity rules
└── .gitattributes         # Git repository configuration
```

### 🛠️ Prerequisites
Make sure you have **Python 3.8+** installed on your system.

```bash
python --version
```

### 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/python-cadastro-2.0.git
   cd python-cadastro-2.0
   ```

2. Run the main entry script:
   ```bash
   python chekout.py
   ```

### 🧩 Module Breakdown
- **`conectar_json.py`**: Utilities to read, write, and update records in `armazenar.json`.
- **`tratamento_input.py`**: Ensures user inputs are formatted correctly.
- **`verificacao_dados.py`**: Validates logical integrity prior to storage.
- **`cores_modelos.py`**: Contains styling constants to provide clean terminal outputs.
- **`destinos.py`**: Maps navigation options and user choices during execution.
- **`chekout.py`**: Handles execution control flow and finalization procedures.

### 📦 Building with PyInstaller
To build a standalone executable from the source code:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Generate the single-file executable using the main script:
   ```bash
   pyinstaller --onefile chekout.py
   ```
The build process artifacts will be generated in `build/`, and the compiled executable will be placed in `dist/`.

---

## 📄 Licença / License

Este projeto está sob a licença MIT / This project is licensed under the MIT License.