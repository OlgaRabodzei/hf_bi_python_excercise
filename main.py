from src.etl import transform_data, aggregate_by_category
from src.local_data_sink import save_data
from src.url_data_source import load_data
import logging

FILE_URL = "https://bnlf-tests.s3.eu-central-1.amazonaws.com/recipes.json"
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def main():
    logger.info("Reading data from %s", FILE_URL)
    raw_data = load_data(FILE_URL)

    logger.info("Transforming data")
    df = transform_data(raw_data)

    logger.info("Saving data")
    save_data(df, "Chilies.csv")

    logger.info("Aggregating data")
    df_grouped = aggregate_by_category(df, "difficulty")

    logger.info("Saving aggregated data")
    save_data(df_grouped, "Results.csv")

    logger.info("Done")


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()
