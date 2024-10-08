import boto3
import pandas as pd
import logging
import psycopg2
from sqlalchemy import create_engine
from io import StringIO
import os

def upload_to_s3(df: pd.DataFrame, bucket_name: str, s3_file_path: str, aws_access_key: str, aws_secret_key: str):
    """Uploads a pandas DataFrame as a CSV to an S3 bucket."""
    try:
        # Convert DataFrame to CSV in-memory
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)

        # Initialize the S3 client
        s3 = boto3.client(
            's3',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key
        )
        
        # Upload CSV to S3
        s3.put_object(Bucket=bucket_name, Key=s3_file_path, Body=csv_buffer.getvalue())
        logging.info(f"Data uploaded successfully to S3 at {bucket_name}/{s3_file_path}")
    except Exception as e:
        logging.error(f"Error occurred while uploading to S3: {e}")
        raise

def load_to_redshift(s3_file_path: str, redshift_table: str, aws_access_key: str, aws_secret_key: str, redshift_credentials: dict):
    """Loads data from an S3 file into an AWS Redshift table using the COPY command."""
    try:
        # Establish connection to Redshift
        conn = psycopg2.connect(
            dbname=redshift_credentials['dbname'],
            user=redshift_credentials['user'],
            password=redshift_credentials['password'],
            host=redshift_credentials['host'],
            port=redshift_credentials['port']
        )
        cur = conn.cursor()

        # Redshift COPY command to load data from S3
        copy_sql = f"""
        COPY {redshift_table}
        FROM 's3://{s3_file_path}'
        ACCESS_KEY_ID '{aws_access_key}'
        SECRET_ACCESS_KEY '{aws_secret_key}'
        CSV
        IGNOREHEADER 1;
        """
        
        # Execute COPY command
        cur.execute(copy_sql)
        conn.commit()
        logging.info(f"Data loaded successfully into Redshift table: {redshift_table}")
    except Exception as e:
        logging.error(f"Error occurred while loading data into Redshift: {e}")
        raise
    finally:
        cur.close()
        conn.close()

