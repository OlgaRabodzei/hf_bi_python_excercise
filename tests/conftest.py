import pytest
import pandas as pd


@pytest.fixture
def data() -> pd.DataFrame:
    df = pd.read_csv('data/sample.csv', index_col=0)
    # Convert the 'duration' columns to Pandas Timedelta
    df['prepTime'] = pd.to_timedelta(df['prepTime'], errors='coerce')
    df['cookTime'] = pd.to_timedelta(df['cookTime'], errors='coerce')
    return df