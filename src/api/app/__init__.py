from flask import Flask
from flask_pydantic_spec import FlaskPydanticSpec

app = Flask(__name__)
spec = FlaskPydanticSpec('Scraping-API')
spec.register(app)

from app.controllers import scraping