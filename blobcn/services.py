from azure.storage.blob import BlobServiceClient
from django.conf import settings

def list_blob_urls():
    # Conectar ao Blob Service Client usando a connection string
    connection_string = settings.CONNECTION_STRING
    container_name = settings.AZURE_CONTAINER

    # Criar o cliente do serviço Blob
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Criar o cliente do container
    container_client = blob_service_client.get_container_client(container_name)

    # Listar os blobs e gerar URLs
    blob_urls = []
    for blob in container_client.list_blobs():
        blob_url = f"https://{settings.AZURE_ACCOUNT_NAME}.blob.core.windows.net/{container_name}/{blob.name}"
        blob_urls.append(blob_url)

    return blob_urls