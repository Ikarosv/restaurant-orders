# restaurant‑orders

**Repositório**: sistema de gerenciamento de pedidos para restaurante.

## Sobre

Um projeto em **Python**, com estrutura de **pacote instalável** e uma suíte de **testes automatizados**, ideal pra gerenciar fluxo de pedidos num ambiente de restaurante digital.

## Estrutura

```text
.
├── data/                 # Arquivos de dados (se houver)
├── src/                  # Código-fonte principal
├── tests/                # Casos de teste automatizados
├── setup.py              # Script de instalação do pacote
├── requirements.txt      # Dependências do projeto
├── dev-requirements.txt  # Dependências para desenvolvimento/testing
└── pyproject.toml        # Metadados do projeto
```

## Instalação

```bash
git clone https://github.com/Ikarosv/restaurant-orders.git
cd restaurant-orders

# Opção 1: instalar diretamente
pip install .

# Opção 2: instalar com dependências dev
pip install -r dev-requirements.txt
```

## Uso

* Executar o módulo principal:

  ```bash
  python -m restaurant_orders
  ```

## Testes

Para rodar os testes automatizados:

```bash
pytest
```

## Contribuição

Contribuições são bem-vindas! Pode abrir issues ou pull requests. Sinta-se à vontade para adicionar funcionalidades, melhorar testes ou aprimorar a cobertura.

