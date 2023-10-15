PYTHON?=python3
PIP?=$(PYTHON) -m pip

run: docker-up
	$(PYTHON) src/main.py

docker-up:
	@docker build -t scraping-api .
	@docker-compose up -d

docker-down:
	@docker stop scraping-api-ctnr
	@docker rm -f scraping-api-ctnr
	@docker rmi scraping-api:latest