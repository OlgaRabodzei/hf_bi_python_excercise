from src.etl import transform_data, aggregate_by_category
from src.local_data_sink import save_data
from src.url_data_source import load_data

FILE_URL = "https://bnlf-tests.s3.eu-central-1.amazonaws.com/recipes.json"


def main():
    raw_data = load_data(FILE_URL)
    df = transform_data(raw_data)
    save_data(df, "Chilies.csv")
    df_grouped = aggregate_by_category(df, "difficulty")
    save_data(df_grouped, "Results.csv")


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()
