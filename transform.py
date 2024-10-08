import pandas as pd
import logging

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans the Iris dataset."""
    try:
        # Handle missing values
        df = df.dropna()

        # Normalize numeric columns
        df['sepal_length'] = (df['sepal_length'] - df['sepal_length'].mean()) / df['sepal_length'].std()
        df['sepal_width'] = (df['sepal_width'] - df['sepal_width'].mean()) / df['sepal_width'].std()
        df['petal_length'] = (df['petal_length'] - df['petal_length'].mean()) / df['petal_length'].std()
        df['petal_width'] = (df['petal_width'] - df['petal_width'].mean()) / df['petal_width'].std()

        # Add a new feature: ratio of petal_length to petal_width
        df['petal_ratio'] = df['petal_length'] / df['petal_width']

        logging.info("Data cleaned successfully")
        return df
    except Exception as e:
        logging.error(f"Error occurred during data transformation: {e}")
        raise

