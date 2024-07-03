import awswrangler as wr
import pandas as pd
import urllib.parse
import os
import time

# Configuration variables
os_input_s3_cleansed_layer = 's3://de-on-youtube-clean-useast1/youtube'
os_input_glue_catalog_db_name = 'db_youtube_cleaned'
os_input_glue_catalog_table_name = 'cleaned_statistics_reference_data'
os_input_write_data_operation = 'append'

def lambda_handler(event, context):
    start_time = time.time()
    print('Lambda function started')

    # Get the object from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    s3_path = f's3://{bucket}/{key}'
    print(f'Bucket: {bucket}, Key: {key}, S3 Path: {s3_path}')
    
    try:
        print(f'Reading data from {s3_path}')
        # Creating DF from content
        df_raw = wr.s3.read_json(s3_path)
        print('Data read successfully from S3')
        print(df_raw.head())  # Print first few rows for debugging

        # Extract required columns
        df_step_1 = pd.json_normalize(df_raw['items'])
        print('Step 1 (data normalization) completed')

        # Write to S3 in Parquet format
        print(f'Writing data to {os_input_s3_cleansed_layer}')
        wr_response = wr.s3.to_parquet(
            df=df_step_1,
            path=os_input_s3_cleansed_layer,
            dataset=True,
            database=os_input_glue_catalog_db_name,
            table=os_input_glue_catalog_table_name,
            mode=os_input_write_data_operation
        )
        print('Data written to S3 in Parquet format')

        end_time = time.time()
        print(f'Lambda function completed in {end_time - start_time} seconds')

        return wr_response

    except Exception as e:
        print(f'Error: {e}')
        print(f'Error getting object {key} from bucket {bucket}. Make sure they exist and your bucket is in the same region as this function.')
        raise e
