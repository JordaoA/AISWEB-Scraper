# AISWEB - Scraper

Esta aplicação fornece informações em tempo real para aeródromos no Brasil. Os dados são obtidos do site [AISWEB](https://www.aisweb.aer.mil.br/) usando web scraping. A aplicação consiste em um pequeno script Python no terminal que interage com um backend dedicado para realizar o scraping e servir os dados coletados de volta ao script principal, que, por sua vez, exibe as informações no terminal.

A ferramenta em questão opera com base em um script principal que analisa as entradas recebidas. Com base nisso, o script pode encerrar a execução, fornecer uma breve descrição da aplicação ou retornar as seguintes informações relacionadas ao código ICAO fornecido:

- Cartas disponíveis.
- Horários de nascer e pôr do sol.
- Informações TAF e METAR disponíveis.

O script principal desempenha o papel de gerenciar as entradas e imprimir na tela os dados coletados referentes a cada código ICAO. O scraping dos dados é realizado por uma API separada, desenvolvida utilizando `Python Flask` para possibilitar a comunicação entre a API e o script principal, e `Docker` para isolar e preparar o ambiente de execução da API responsável pelo scraping. O scraping dos dados é feito usando as bibliotecas Beautiful Soup (`Bs4`) e `requests` do Python. Todo o ambiente necessário para o funcionamento da API é preparado por meio do uso de `Docker` e `Docker Compose`. A rota de scraping está disponível para utilização por meio do Swagger na URL [localhost:5000/apidoc/swagger](http://localhost:5000/apidoc/swagger).

## Como Usar

### Pré-requisitos

- Certifique-se de ter o `Python 3.10` instalado em seu sistema.
- Tenha o `Docker` instalado para executar o backend como um contêiner.
- Tenha o `Docker Compose` instalado para executar o backend responsável pelo scraper.
- Tenha o utilitário `Make` instalado para possibilitar a execução automatizada da aplicação.

### Configuração

- Clone o repositório:

   ```bash
   git clone https://github.com/JordaoA/AISWEB-Scraper.git
   cd AISWEB-Scraper
   ```

A partir deste ponto, você já pode começar a usar o scraper.

### Utilizando a ferramenta

Com todos os pré-requisitos instalados, para usar o scraper, siga os comandos a seguir:

- `make build` (prepara e executa o contêiner da API responsável pelo scraping).
- `make run` (executa o script que coleta informações com base no código ICAO).
- `make down` (encerra o contêiner da API de scraping).

Se você não puder usar o `Make` para automatizar o processo, siga os comandos a seguir:

```bash
# Para iniciar o backend (API) responsável pelo scraping.
docker build -t scraping-api .
docker-compose up -d
```

```bash
#Para rodar o script que recolhe o código ICAO
python3 src/main.py
```
 
```bash
# Para interromper o funcionamento da aplicação
docker stop scraping-api-ctnr
docker rm -f scraping-api-ctnr
docker rmi scraping-api:latest
```

A partir deste ponto, você só precisa fornecer o código ICAO que deseja usar como base para coletar as informações.

#### Informações adicionais

Se desejar encerrar o uso da aplicação principal, basta inserir "sair" no prompt de entrada da aplicação, e o script será encerrado. O prompt também exibirá uma breve explicação na tela quando você inserir "ajuda" no prompt de entrada.
