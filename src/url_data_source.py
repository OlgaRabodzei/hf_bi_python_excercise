import requests
import json
import pandas as pd


def load_data(file_url: str) -> pd.DataFrame:
    response = requests.get(file_url)
    response.raise_for_status()

    raw_data = response.content.decode("utf-8").splitlines()
    raw_data = [json.loads(row) for row in raw_data]
    df = pd.DataFrame(raw_data)
    # Convert the 'duration' columns to Pandas Timedelta
    df['prepTime'] = pd.to_timedelta(df['prepTime'], errors='coerce')
    df['cookTime'] = pd.to_timedelta(df['cookTime'], errors='coerce')

    return df
