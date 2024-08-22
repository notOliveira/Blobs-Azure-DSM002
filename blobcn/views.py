# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .services.blob_services import list_blob_urls
from .services.tables_services import AzureTableService
import json

table_service = AzureTableService()

def index(request):
    return render(request, 'blobcn/index.html')

# Blob Storage Views
def storage(request):
    blob_urls = list_blob_urls()
    return render(request, 'blobcn/storage.html', {'blob_urls': blob_urls})

table_service = AzureTableService()

# List entities view
def list_entities_view(request):
    entities = table_service.list_entities()
    return render(request, 'blobcn/list_entities.html', {'entities': entities})

# Create entity view
@csrf_exempt
@require_http_methods(["POST"])
def create_entity_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        partition_key = data.get('PartitionKey')
        row_key = data.get('RowKey')
        properties = {k: v for k, v in data.items() if k not in ['PartitionKey', 'RowKey']}
        table_service.create_entity(partition_key, row_key, **properties)
        return redirect('list_entities')  # Redireciona para a página de listagem após criação

# Read entity view
@require_http_methods(["GET"])
def read_entity_view(request, partition_key, row_key):
    entity = table_service.read_entity(partition_key, row_key)
    return render(request, 'blobcn/read_entity.html', {'entity': entity})

# Update entity view
@csrf_exempt
@require_http_methods(["PUT"])
def update_entity_view(request, partition_key, row_key):
    data = json.loads(request.body)
    table_service.update_entity(partition_key, row_key, **data)
    return redirect('list_entities')  # Redireciona para a página de listagem após atualização

# Delete entity view
@csrf_exempt
@require_http_methods(["DELETE"])
def delete_entity_view(request, partition_key, row_key):
    table_service.delete_entity(partition_key, row_key)
    return redirect('list_entities')  # Redireciona para a página de listagem após deleção