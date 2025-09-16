# main.py
from fastapi import FastAPI
from dotenv import load_dotenv
import os
import requests

load_dotenv() # Carga las variables de entorno del archivo .env

app = FastAPI()

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
PLACES_API_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

@app.get("/api/motels")
def get_nearby_motels(lat: float, lon: float, radius: int = 5000): # radio en metros
    params = {
        "location": f"{lat},{lon}",
        "radius": radius,
        "type": "lodging", # 'lodging' es una categoría amplia, se puede ajustar
        "keyword": "motel", # Buscamos específicamente por la palabra "motel"
        "key": GOOGLE_MAPS_API_KEY
    }
    
    response = requests.get(PLACES_API_URL, params=params)
    response.raise_for_status() # Lanza un error si la petición falla
    
    # Aquí puedes añadir lógica para filtrar y limpiar los datos antes de enviarlos
    return response.json()