# restaurant‑orders

**Repositório**: sistema de gerenciamento de pedidos para restaurante desenvolvido no curso da Trybe.

## 🧾 Sobre

Projeto em **Python**, com estrutura de **pacote instalável**, uso de **testes automatizados** e foco na lógica de gerenciamento de pedidos em restaurantes.

## 📦 Tecnologias e bibliotecas utilizadas

* **Python 3.8+**
* **pytest** – para testes
* **flake8** – para análise de estilo de código

## 🗂️ Estrutura do projeto

```
.
├── data/                 # Arquivos de dados (CSV, etc)
├── src/restaurant_orders/  # Código-fonte principal
├── tests/                # Testes automatizados
├── setup.py              # Script de instalação
├── requirements.txt      # Dependências da aplicação
├── dev-requirements.txt  # Dependências para desenvolvimento/testes
└── pyproject.toml        # Configurações de build e metadata
```

## 🚀 Instalação

```bash
git clone https://github.com/Ikarosv/restaurant-orders.git
cd restaurant-orders

# Instalar o pacote
pip install .

# Instalar dependências de desenvolvimento
pip install -r dev-requirements.txt
```

## ⚙️ Como usar

Execute o programa via CLI:

```bash
python -m restaurant_orders path/to/data.csv
```

## 🧪 Testes

Para rodar os testes com `pytest`:

```bash
pytest
```

Com relatório de cobertura:

```bash
coverage run -m pytest
coverage report -m
```

## 🤝 Contribuindo

Contribuições são bem-vindas!
Abra uma issue, fork o repositório e envie um pull request com melhorias ou correções.
