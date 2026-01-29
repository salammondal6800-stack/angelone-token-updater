import requests
import csv
import json
from datetime import datetime

URL = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"

def fetch_data():
    print("Downloading instrument list...")
    response = requests.get(URL)
    response.raise_for_status()
    return response.json()

def save_csv(data):
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"angelone_instruments_{today}.csv"

    keys = data[0].keys()

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    print(f"Saved file: {filename}")

if __name__ == "__main__":
    data = fetch_data()
    save_csv(data)
