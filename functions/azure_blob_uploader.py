import io
import os
from dotenv import load_dotenv
import pandas as pd
from azure.storage.blob import BlobServiceClient, ContentSettings

load_dotenv()

output = io.StringIO()

storage_account_name = os.environ['accountName']
storage_account_key = os.environ['accountKey']
container_name = os.environ['containerName']

def save_dataframe_to_blob(df, blob_name):
    try:
        # Convert DataFrame to CSV string
        csv_data = df.to_csv(index=False)

        # Create a BlobServiceClient
        blob_service_client = BlobServiceClient(account_url=f"https://{storage_account_name}.blob.core.windows.net", credential=storage_account_key)

        # Get a reference to a container
        container_client = blob_service_client.get_container_client(container_name)

        # Upload data to Blob Storage
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.upload_blob(csv_data, content_settings=ContentSettings(content_type='application/csv'),overwrite=True)

        print(f"DataFrame successfully saved to Azure Blob Storage. Container: {container_name}, Blob: {blob_name}")

        return f"https://{storage_account_name}.blob.core.windows.net/{container_name}/{blob_name}"

    except Exception as e:
        print(f"Error: {e}")
