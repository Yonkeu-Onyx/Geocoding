🇬🇧 [English version](README.md)

# API de géocodage inversé

Une API REST légère construite avec **FastAPI**, qui convertit des coordonnées GPS (latitude/longitude) en données de localisation lisibles, à l'aide de l'**API Google Maps Geocoding**.

## Contexte

Construite dans le cadre d'un stage, pour le backend d'une application mobile qui devait convertir les coordonnées d'un utilisateur en nom de ville/région.

## Fonctionnalités

- `/getAll` — retourne la réponse brute complète de Google Maps pour des coordonnées données
- `/getcity` — retourne uniquement le nom de la ville/région, extrait des composantes d'adresse
- CORS activé pour faciliter l'intégration avec un frontend ou une application mobile
- Configuration de la clé API via variables d'environnement (aucun secret en dur dans le code)

## Stack technique

- **Python 3** / **FastAPI**
- **API Google Maps Geocoding**
- **Pydantic** pour la validation des requêtes
- **Docker** pour le déploiement

## Installation locale

```bash
# Cloner le repo
git clone https://github.com/Yonkeu-Onyx/Geocoding.git
cd Geocoding

# Installer les dépendances
pip install -r requirements.txt

# Configurer la clé API
cp .env.example .env
# puis ajouter ta clé MAPS_API_KEY dans .env (à obtenir sur Google Cloud Console)

# Lancer le serveur
uvicorn main:app --reload
```

L'API sera disponible sur `http://localhost:8000`, avec une documentation interactive sur `http://localhost:8000/docs`.

## Utilisation

**POST** `/getcity`

```json
{
  "latitude": "45.5019",
  "longitude": "-73.5674"
}
```

**Réponse :**

```json
{
  "city": "Montréal"
}
```

**POST** `/getAll` accepte le même corps de requête et retourne la réponse complète de Google Maps (toutes les composantes d'adresse, adresses formatées, identifiants de lieu, etc.).

## Ce que j'ai appris sur ce projet

- Consommer et parser une réponse d'API tierce réelle (structure imbriquée `address_components` de Google Maps)
- Extraire une donnée précise d'une réponse JSON profondément imbriquée selon plusieurs critères de correspondance (`types` contenant à la fois `administrative_area_level_2` et `political`)
- Structurer une petite API autour d'endpoints clairs à responsabilité unique

## Licence

Projet personnel à but éducatif.
