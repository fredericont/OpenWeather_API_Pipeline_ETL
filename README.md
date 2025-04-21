# Weather ETL Project

## 📌 Descrição

Este projeto foi desenvolvido como uma prática de engenharia de dados, com o objetivo de **extrair, transformar e carregar (ETL)** dados de previsão do tempo para a cidade de **Natal-RN**, utilizando a API da **OpenWeatherMap**.

### O pipeline realiza as seguintes etapas:

- **Extração:** Obtém dados de previsão do tempo (temperatura, umidade, etc.) para Natal-RN usando a API da OpenWeatherMap.  
- **Transformação:** Processa os dados extraídos, convertendo temperaturas de Kelvin para Celsius e organizando-os em um DataFrame com **Pandas**.  
- **Visualização:** Gera gráficos para análise da variação de temperatura e umidade ao longo do tempo.  
- **Carga:** Armazena os dados processados em um banco de dados **PostgreSQL**, funcionando como um Data Warehouse básico.

> Este projeto foi implementado em ambiente **Linux (Ubuntu)** com **Jupyter Notebook**, voltado para profissionais de dados que desejam praticar pipelines ETL e visualização de dados.

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

### `secrets.json`  
Contém a chave da API da OpenWeatherMap:

```json
{
  "WEATHER_API_KEY": "api_key_openweather"
}
```

### `db_config.json`  
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

Este projeto foi desenvolvido para rodar em ambiente **Linux (Ubuntu)** com **Jupyter Notebook já instalado**. As bibliotecas utilizadas são nativas do ambiente padrão do Jupyter, portanto **não é necessário instalar pacotes adicionais**, a menos que esteja utilizando um ambiente customizado ou limpo.

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

- Atualize o arquivo `db_config.json` com suas credenciais.  
- Obtenha uma chave de API da OpenWeatherMap e atualize o arquivo `secrets.json`.

---

### 2. Executando o Projeto

Abra o Jupyter Notebook:

```bash
jupyter notebook weather_etl.ipynb
```

Execute as células na ordem:

1. Importa as bibliotecas necessárias  
2. Faz requisição à API da OpenWeatherMap  
3. Exibe os dados brutos retornados pela API  
4. Processa e organiza os dados em um DataFrame  
5. Gera gráfico de variação de temperatura  
6. Gera gráfico de variação de umidade  
7. Conecta ao PostgreSQL  
8. Cria a tabela `weather_data`  
9. Insere os dados processados na tabela

---

### 3. Resultados Esperados

#### 📊 Gráficos

- **Temperatura:** Variação ao longo do tempo com linha de média  
- **Umidade:** Variação relativa ao longo do tempo

#### 🗄️ Banco de Dados

- Os dados serão salvos na tabela `weather_data`, contendo colunas como:
  - `DateTime`
  - `Temperature (°C)`
  - `Humidity (%)`
  - Entre outras

---

## 📁 Estrutura do Repositório

```
weather_etl.ipynb      # Notebook principal contendo o pipeline ETL
secrets.json           # Chave da API (não versionado)
db_config.json         # Configuração do banco (não versionado)
README.md              # Este arquivo
```

---

## 🌟 Possíveis Melhorias

- Adicionar mais visualizações (ex.: pressão atmosférica, velocidade do vento)
- Implementar agendamento para atualização automática (ex.: `schedule` ou `cron`)
- Adicionar tratamento de erros mais robusto para falhas na API ou no banco
- Incluir testes unitários para validar o pipeline ETL

---

## 👤 Autor

Desenvolvido por **Francisco Frederico**, engenheiro/analista de dados, como parte de um exercício prático de engenharia de dados.

---

## ⚠️ Notas Finais

- Certifique-se de que os arquivos `secrets.json` e `db_config.json` **não sejam versionados** no GitHub. Use `.gitignore` para protegê-los.  
- Caso encontre problemas, verifique se o PostgreSQL está rodando e se as credenciais estão corretas.

---

## 🔗 Referências

- [OpenWeatherMap - Call 5 day / 3 hour forecast data](https://openweathermap.org/forecast5):  
  Esta documentação foi utilizada para configurar a chamada à API de previsão do tempo de 5 dias com intervalos de 3 horas, que fornece os dados utilizados na etapa de extração do pipeline ETL.
