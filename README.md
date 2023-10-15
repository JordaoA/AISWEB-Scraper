# AISWEB - Scraper

Esta aplicação fornece informações em tempo real para aeródromos no Brasil. Os dados são obtidos do site [AISWEB](https://www.aisweb.aer.mil.br/) usando web scraping. A aplicação consiste em um pequeno script no terminal em Python que interage com um backend que realiza o scraping e serve os dados coletados para o script principal, e lá acontece a exibição no terminal.

A ferramente em questão funciona com base em um script principal, que diferencia as entradas que recebe, e a partir disso, pode encerrar o funcionamento do script, descrever a aplicação brevemente, ou nos retornar as seguintes informações ligadas ao código ICAO fornecido:
- As cartas disponíveis.
- Horários de nascer e pôr do sol.
- Informações de TAF e METAR disponíveis.

Aqui o script principal faz o papel de gerir as entradas e imprimir na tela os dados coletados, referente a cada código ICAO. O Scraping dos dados é feito por uma API a parte. Essa API foi feita utilizando `Python Flask` (para tornanr possivel a comunicação entre a API e o script principal) e `Docker` (isola e prepara o ambiente de funcionamento da API responsável pelo scraping). O Scraping dos dados foi feito usando as bibliotecas `Bs4` (Beautiful Soup) e `requests` do `Python`. Todo o ambiente necessário para o funcionamento da API é preparado através do uso de Docker e Docker compose.
A rota de sraping está disponível para uso através do Swagger na url [localhost:5000/apidoc/swagger](http://localhost:5000/apidoc/swagger).

## Como Usar

### Pré-requisitos

- Certifique-se de ter o `Python 3.10` instalado em seu sistema.
- Tenha o `Docker` instalado para executar o backend como um contêiner.
- Tenha o `Docker-compose` instalado, também para executar o backend responsável pelo scraper.
- Tenha o `Make` instalado para que seja possível a execução automatizada da aplicação. 

### Configuração

- Clone o repositório:

   ```bash
   git clone https://github.com/JordaoA/AISWEB-Scraper.git
   cd AISWEB-Scraper
   ```

A partir daqui já é possivel usar o scraper.

### Utilizando ferramenta

Com todos os prerequisitos instalados, para utilizar o scraper, nós devemos utilizar os comandos:
- `make build` (prepara e executa o container da API responsável pelo scraping).
- `make run` (roda o script que recolhe o código ICAO).
- `make down` (derruba o container com a API de scraping).

Caso não seja possível utilizar o `Make` para automatizar o processo, siga os seguintes comandos:


```bash
    # Para subir o Backend (API) responsável pelo scraping.
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

A partir disso, só precisamos fornecer o codigo ICAO que desejamos usar como base para recolher as informações.

#### Informações extra

Se quisermos encerrar o uso da aplicação pricipal, podemos aprenas fornecer a `sair` no prompt de entrada da aplicação e o script sera encerrado. O prompt também imprime na tela uma breve explicação quando recebe `ajuda` no prompt de entrada.
