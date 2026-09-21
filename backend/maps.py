from config import MAPS_API_KEY

def build_map_request(city: str) -> dict:
    return {
        "provider": "AtlasMaps",
        "city": city,
        "api_key": MAPS_API_KEY
    }
