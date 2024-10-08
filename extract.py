import pandas as pd
import logging

def extract_data(file_path: str) -> pd.DataFrame:
    """Extracts data from a CSV file into a pandas DataFrame."""
    try:
        df = pd.read_csv(file_path)
        logging.info(f"Data extracted successfully from {file_path}")
        return df
    except Exception as e:
        logging.error(f"Error occurred while extracting data: {e}")
        raise

