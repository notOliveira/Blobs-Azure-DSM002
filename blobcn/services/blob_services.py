from azure.storage.blob import BlobServiceClient
from django.conf import settings

def list_blob_urls():
    connection_string = settings.CONNECTION_STRING  # Use a connection string para Blob Storage
    container_name = settings.AZURE_CONTAINER

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    blob_urls = []
    for blob in container_client.list_blobs():
        blob_url = f"https://{settings.AZURE_ACCOUNT_NAME}.blob.core.windows.net/{container_name}/{blob.name}"
        blob_urls.append(blob_url)

    return blob_urls