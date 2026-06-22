import pandas as pd
import requests
from pathlib import Path

SAVE_PATH = Path("Data/raw")

scheme_id = 119551

url = f"https://api.mfapi.in/mf/{scheme_id}"

response = requests.get(url)

data = response.json()

nav_df = pd.DataFrame(data["data"])

nav_df.to_csv(
    SAVE_PATH / "live_nav.csv",
    index=False
)

print(nav_df.head())
print("NAV data saved successfully")