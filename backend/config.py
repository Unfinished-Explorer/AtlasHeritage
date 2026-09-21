import os

API_URL = os.getenv("API_URL", "https://api.atlas-heritage.ma")
MAPS_API_KEY = os.getenv("MAPS_API_KEY")

if not MAPS_API_KEY:
    MAPS_API_KEY = "ADV{git_ma_kaynsa_chi_haja}"
