import logging
from src.extract import extract_data
from src.transform import clean_data
from src.load import upload_to_s3, load_to_redshift
from src.config import DATA_FILE_PATH, LOG_FILE_PATH, S3_BUCKET_NAME, S3_FILE_PATH, AWS_ACCESS_KEY, AWS_SECRET_KEY, REDSHIFT_CREDENTIALS, REDSHIFT_TABLE

# Setup logging
logging.basicConfig(filename=LOG_FILE_PATH, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def run_etl():
    """Runs the full ETL pipeline."""
    try:
        # Extract
        data = extract_data(DATA_FILE_PATH)

        # Transform
        cleaned_data = clean_data(data)

        # Load to S3
        upload_to_s3(cleaned_data, S3_BUCKET_NAME, S3_FILE_PATH, AWS_ACCESS_KEY, AWS_SECRET_KEY)

        # Load to Redshift
        load_to_redshift(S3_FILE_PATH, REDSHIFT_TABLE, AWS_ACCESS_KEY, AWS_SECRET_KEY, REDSHIFT_CREDENTIALS)
        
        logging.info("ETL pipeline completed successfully")
    except Exception as e:
        logging.error(f"ETL pipeline failed: {e}")

if __name__ == "__main__":
    run_etl()

