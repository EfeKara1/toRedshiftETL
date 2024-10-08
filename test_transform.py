import pandas as pd
from src.transform import clean_data

def test_clean_data():
    # Mocked DataFrame similar to the Iris dataset
    data = {
        'sepal_length': [5.1, 4.9, 4.7, 4.6],
        'sepal_width': [3.5, 3.0, 3.2, 3.1],
        'petal_length': [1.4, 1.4, 1.3, 1.5],
        'petal_width': [0.2, 0.2, 0.2, 0.2],
        'species': ['setosa', 'setosa', 'setosa', 'setosa']
    }
    df = pd.DataFrame(data)
    
    transformed_df = clean_data(df)
    
    # Assert that new column was added
    assert 'petal_ratio' in transformed_df.columns

