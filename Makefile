PYTHON?=python3
PIP?=$(PYTHON) -m pip

run:
	$(PYTHON) src/main.py

build:
	@docker build -t scraping-api .
	@docker-compose up -d

down:
	@docker stop scraping-api-ctnr
	@docker rm -f scraping-api-ctnr
	@docker rmi scraping-api:latest
