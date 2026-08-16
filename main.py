import base64
import json
import os
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()


MAPS_API_KEY = os.environ.get("MAPS_API_KEY")

maps_base_url = "https://maps.googleapis.com/maps/api/geocode/json?"
headers = {
    "Content-Type": "application/json",
}
    
class LocationRequest(BaseModel):
    latitude: str
    longitude: str


@app.post("/getAll")
def getAll(location : LocationRequest):
    lat = float(location.latitude)
    lon = float(location.longitude)
    response = requests.get(f'{maps_base_url}latlng={lat},{lon}&key={MAPS_API_KEY}', headers=headers)
    data = response.json()

    return data

@app.post("/getcity")
def get_city(location : LocationRequest):
    print(f'Latitude: {location.latitude}')
    print(f'Longitude: {location.longitude}')
    lat = float(location.latitude)
    lon = float(location.longitude)
    response = requests.get(f'{maps_base_url}latlng={lat},{lon}&key={MAPS_API_KEY}', headers=headers)
    data = response.json()
    city_name = extract_region_long_name(data)
    name = {
        "city": city_name
    }

    return name


def extract_region_long_name(data):
    """
    Extracts the long_name from address_components where types contains 
    both 'administrative_area_level_2' and 'political'.
    Returns the first match found or None if not found.
    """
    for result in data.get("results", []):
        for component in result.get("address_components", []):
            types = component.get("types", [])
            if "administrative_area_level_2" in types and "political" in types:
                return component.get("long_name")
    return None