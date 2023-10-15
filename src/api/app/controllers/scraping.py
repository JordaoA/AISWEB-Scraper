from app import app, spec
from flask import request, jsonify
from flask_pydantic_spec import (Response, Request)

from app.services.scraping import AiswebData


@app.get('/scrap-data/<string:icao_code>')
@spec.validate(tags=["Scraping"])
def scrapi_data(icao_code):
    """
    - GET method to scrapi all data.
    """
    scrap_obj = AiswebData(icao_code)
    aisweb_data = scrap_obj.scrap_data()
    
    if aisweb_data.get('error'):
        return jsonify(aisweb_data), 404
    else:
        return jsonify(aisweb_data), 200