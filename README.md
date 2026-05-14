# 🌦️ Pipeline Climático — São Paulo

Pipeline de dados completo que coleta dados climáticos em tempo real de São Paulo, processa com Python e pandas, armazena no PostgreSQL e visualiza em um dashboard no Power BI — atualizado automaticamente de hora em hora.

---

## 🏗️ Arquitetura do Projeto

```
API OpenWeatherMap → Python + pandas → PostgreSQL → Power BI
                                ↑
                        Task Scheduler (1h)
```

---

## 🔧 Stack Utilizada

- **Python** — coleta e processamento dos dados
- **pandas** — transformação e limpeza
- **SQLAlchemy + psycopg2** — conexão com o banco de dados
- **PostgreSQL** — armazenamento dos dados
- **Power BI** — visualização em dashboard
- **Windows Task Scheduler** — automação da execução

---

## 📊 Dados Coletados

| Campo | Descrição |
|---|---|
| Cidade | Nome da cidade monitorada |
| Temperatura (ºC) | Temperatura atual |
| Condição Atual | Descrição do tempo (ex: céu limpo) |
| Umidade (%) | Percentual de umidade do ar |
| Nascer do Sol | Horário do nascer do sol |
| Pôr do Sol | Horário do pôr do sol |
| Data/Hora | Timestamp da coleta |

---

## ⚙️ Como Rodar

### Pré-requisitos
- Python 3.11+
- PostgreSQL instalado e rodando
- Conta na [OpenWeatherMap API](https://openweathermap.org/api) (gratuita)

### Instalação

```bash
pip install pandas requests sqlalchemy psycopg2-binary python-dotenv
```

### Configuração

Cria um arquivo `.env` na pasta do projeto:

```
API_KEY=sua_chave_aqui
DB_PASSWORD=sua_senha_aqui
```

### Execução

```bash
python CLIMA.py
```

---

## 🤖 Automação

O script é agendado via **Windows Task Scheduler** para rodar automaticamente de hora em hora, mantendo o banco de dados e o dashboard sempre atualizados sem nenhuma intervenção manual.

---

## 📁 Estrutura do Projeto

```
CLIMA_PIPELINE/
├── CLIMA.py        # Script principal do pipeline
├── .env            # Credenciais (não versionado)
├── .gitignore      # Ignora o .env
└── README.md       # Documentação
```

---

## 👨‍💻 Autor

**Lucas Zanella Clemente**  
Estudante de Engenharia de Software — FIAP  
[LinkedIn](https://www.linkedin.com/in/lucas-zanella-777-dev/) | [GitHub](https://github.com/LucasZanellaClemente)
