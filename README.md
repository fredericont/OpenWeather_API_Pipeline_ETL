
# Weather ETL Project

## 📌 Descrição

Este projeto foi desenvolvido como uma prática de engenharia de dados, com o objetivo de **extrair, transformar e carregar (ETL)** dados de previsão do tempo para a cidade de **Natal-RN**, utilizando a API da **OpenWeatherMap**.

### O pipeline realiza as seguintes etapas:

- **Extração:** Obtém dados de previsão do tempo (temperatura, umidade, etc.) para Natal-RN usando a API da OpenWeatherMap.  
- **Transformação:** Processa os dados extraídos, convertendo temperaturas de Kelvin para Celsius e organizando-os em um DataFrame com **Pandas**.  
- **Visualização (apenas no Jupyter Notebook):** Gera gráficos para análise da variação de temperatura e umidade ao longo do tempo.  
- **Carga:** Armazena os dados processados em um banco de dados **PostgreSQL**, funcionando como um Data Warehouse básico.

> Este projeto foi implementado em ambiente **Linux (Ubuntu)**, com suporte tanto para execução interativa via **Jupyter Notebook** quanto para automação via script Python. Voltado para profissionais de dados que desejam praticar pipelines ETL e visualização de dados.

---

## 🧰 Requisitos

### ✅ Sistema Operacional

- Linux (desenvolvido e testado no Ubuntu)

### ✅ Dependências

- Python 3.8 ou superior  
- Bibliotecas Python (instaláveis via `pip`):

```bash
pip install pandas requests matplotlib seaborn psycopg2 sqlalchemy
```

- PostgreSQL instalado e configurado  
- Chave de API válida da OpenWeatherMap

---

## 📄 Arquivos Necessários

### `config/secrets.json`  
Contém a chave da API da OpenWeatherMap:

```json
{
  "WEATHER_API_KEY": "api_key_openweather"
}
```

### `config/db_config.json`  
Contém as credenciais de acesso ao banco PostgreSQL:

```json
{
  "user": "postgres",
  "password": "password_here",
  "host": "localhost",
  "port": "5432",
  "database": "database_name_here"
}
```

---

## 🚀 Como Usar

### 1. Configuração do Ambiente

Clone este repositório para sua máquina local:

```bash
git clone https://github.com/fredericont/OpenWeather_API_Pipeline_ETL
cd OpenWeather_API_Pipeline_ETL
```

Este projeto foi desenvolvido para rodar em ambiente **Linux (Ubuntu)**. Para execução interativa, utiliza-se o **Jupyter Notebook** (`weather_etl.ipynb`). Para automação, utiliza-se o script Python (`weather_etl.py`). As bibliotecas necessárias são instaláveis via `pip`.

> Caso o Jupyter não esteja instalado, você pode instalá-lo com:

```bash
sudo apt update
sudo apt install jupyter
```

> Ou, se estiver usando `pip`:

```bash
pip install notebook
```

Configure o PostgreSQL:

- Certifique-se de que o PostgreSQL está rodando.  
- Crie um banco de dados para o projeto:

```sql
CREATE DATABASE nome_do_banco;
```

- Atualize o arquivo `config/db_config.json` com suas credenciais.  
- Obtenha uma chave de API da OpenWeatherMap e atualize o arquivo `config/secrets.json`.

---

### 2. Executando o Projeto

#### Opção 1: Execução Interativa (Jupyter Notebook)

Abra o Jupyter Notebook:

```bash
jupyter notebook etl/weather_etl.ipynb
```

Execute as células na ordem:

1. Importa as bibliotecas necessárias  
2. Faz requisição à API da OpenWeatherMap  
3. Exibe os dados brutos retornados pela API  
4. Processa e organiza os dados em um DataFrame  
5. Exibe o `head` do DataFrame para inspeção  
6. Gera gráfico de variação de temperatura  
7. Gera gráfico de variação de umidade  
8. Conecta ao PostgreSQL  
9. Cria a tabela `weather_data`  
10. Insere os dados processados na tabela

> **Nota:** O Jupyter Notebook (`weather_etl.ipynb`) é ideal para exploração de dados, visualização de gráficos e validação interativa do pipeline ETL.

#### Opção 2: Execução Automatizada (Script Python)

Execute o script Python diretamente:

```bash
python etl/weather_etl.py
```

Este script realiza o mesmo processo ETL (extração, transformação e carga), mas sem gerar visualizações ou exibir o `head` do DataFrame. É ideal para integração em pipelines automatizados ou agendamentos (ex.: `cron`).

> **Motivo para manter ambos os arquivos:**  
> - O arquivo `weather_etl.ipynb` é voltado para **análise interativa**, permitindo que o usuário visualize os dados processados (via `head` do DataFrame) e os gráficos gerados (temperatura e umidade). É útil para desenvolvimento, validação e ensino.  
> - O arquivo `weather_etl.py` é otimizado para **execução automatizada**, sem dependência de interfaces gráficas ou interação manual. Ele é mais leve e adequado para cenários de produção, como agendamentos ou integração com outros sistemas.  
> Essa dualidade atende tanto a profissionais que desejam explorar os dados quanto a pipelines automatizados em ambientes operacionais.

---

### 3. Resultados Esperados

#### 📊 Gráficos (apenas no Jupyter Notebook)

- **Temperatura:** Variação ao longo do tempo com linha de média  
- **Umidade:** Variação relativa ao longo do tempo

#### 🗄️ Banco de Dados

- Os dados serão salvos na tabela `weather_data`, contendo colunas como:
  - `DateTime`
  - `Temperature (°C)`
  - `Humidity (%)`
  - Entre outras

---

![image](https://github.com/user-attachments/assets/f383eca0-93f7-4aab-b63a-685532bacd83)
![image](https://github.com/user-attachments/assets/de1e560b-7c81-4707-b3ff-8dcb2cfbb24c)

## 📁 Estrutura do Repositório

```
.
├── config/
│   ├── db_config.json        # Credenciais do banco PostgreSQL
│   └── secrets.json          # Chave da API OpenWeatherMap
├── database/
│   └── db_connection.py      # Função de conexão e execução de queries no banco
├── etl/
│   ├── weather_etl.ipynb     # Jupyter Notebook com gráficos e análise interativa
│   └── weather_etl.py        # Script automatizado de ETL (sem visualizações)
├── utils/
│   └── helpers.py            # Funções auxiliares para transformação e carregamento
└── README.md                 # Este arquivo
```

---

## 🌟 Possíveis Melhorias

- Adicionar mais visualizações (ex.: pressão atmosférica, velocidade do vento) no Jupyter Notebook
- Implementar agendamento para atualização automática no script Python (ex.: `schedule` ou `cron`)
- Adicionar tratamento de erros mais robusto para falhas na API ou no banco
- Incluir testes unitários para validar o pipeline ETL
- Modularizar ainda mais o código, separando funções de extração, transformação e carga

---

## 👤 Autor

Desenvolvido por **Francisco Frederico**, engenheiro/analista de dados, como parte de um exercício prático de engenharia de dados.

---

## ⚠️ Notas Finais

- Certifique-se de que os arquivos `config/secrets.json` e `config/db_config.json` **não sejam versionados** no GitHub. Use `.gitignore` para protegê-los.  
- Caso encontre problemas, verifique se o PostgreSQL está rodando e se as credenciais estão corretas.

---

## 🔗 Referências

- [OpenWeatherMap - Call 5 day / 3 hour forecast data](https://openweathermap.org/forecast5):  
  Esta documentação foi utilizada para configurar a chamada à API de previsão do tempo de 5 dias com intervalos de 3 horas, que fornece os dados utilizados na etapa de extração do pipeline ETL.
