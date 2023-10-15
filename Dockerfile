FROM python:3.10-alpine

WORKDIR /scrapi-api/

COPY /src/api /scrapi-api/api
COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["api/run.py"]