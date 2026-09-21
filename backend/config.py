import os

API_URL = os.getenv("API_URL", "https://api.atlas-heritage.ma")

MAPS_API_KEY = os.getenv("MAPS_API_KEY")

if not MAPS_API_KEY:
    raise RuntimeError(
        "MAPS_API_KEY environment variable is required but not defined."
    )
