import os

# Configuration file for file paths and credentials
DATA_FILE_PATH = os.path.join('data', 'iris.csv')
LOG_FILE_PATH = os.path.join('logs', 'etl.log')

# AWS Credentials (replace with your own)
AWS_ACCESS_KEY = 'YOUR_AWS_ACCESS_KEY'
AWS_SECRET_KEY = 'YOUR_AWS_SECRET_KEY'
S3_BUCKET_NAME = 'your-s3-bucket'
S3_FILE_PATH = 'data/iris.csv'

# Redshift Credentials (replace with your own)
REDSHIFT_CREDENTIALS = {
    'dbname': 'your_redshift_db',
    'user': 'your_redshift_user',
    'password': 'your_redshift_password',
    'host': 'your_redshift_cluster_host',
    'port': 5439
}
REDSHIFT_TABLE = 'iris_data'

