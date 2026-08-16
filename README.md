🇫🇷 [Version française](README.fr.md)

# Reverse Geocoding API

A lightweight REST API built with **FastAPI** that converts GPS coordinates (latitude/longitude) into human-readable location data, using the **Google Maps Geocoding API**.

## Context

Built during an internship, as part of the backend for a mobile application that needed to resolve a user's coordinates into a city/region name.

## Features

- `/getAll` — returns the full raw geocoding response from Google Maps for a given lat/lon
- `/getcity` — returns just the city/region name, extracted from the address components
- CORS enabled for easy integration with a frontend or mobile app
- Environment-based API key configuration (no hardcoded secrets)

## Tech stack

- **Python 3** / **FastAPI**
- **Google Maps Geocoding API**
- **Pydantic** for request validation
- **Docker** for deployment

## Local setup

```bash
# Clone the repo
git clone https://github.com/Yonkeu-Onyx/Geocoding.git
cd Geocoding

# Install dependencies
pip install -r requirements.txt

# Configure your API key
cp .env.example .env
# then add your MAPS_API_KEY in .env (get one from the Google Cloud Console)

# Run the server
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`, with interactive docs at `http://localhost:8000/docs`.

## Usage

**POST** `/getcity`

```json
{
  "latitude": "45.5019",
  "longitude": "-73.5674"
}
```

**Response:**

```json
{
  "city": "Montréal"
}
```

**POST** `/getAll` accepts the same body and returns the complete Google Maps geocoding response (all address components, formatted addresses, place IDs, etc.).

## What I learned building this

- Consuming and parsing a real-world third-party API response (Google Maps' nested `address_components` structure)
- Extracting specific data from a deeply nested JSON response based on multiple matching criteria (`types` containing both `administrative_area_level_2` and `political`)
- Structuring a small API around clear, single-purpose endpoints

## License

Personal project for educational purposes.
