import pandas as pd
import requests
from pathlib import Path

SAVE_PATH = Path("Data/raw")
SAVE_PATH.mkdir(parents=True, exist_ok=True)

scheme_codes = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in scheme_codes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    nav_df.to_csv(
        SAVE_PATH / f"{name}_nav.csv",
        index=False
    )

    print(f"Saved {name} NAV Data")