# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .services.blob_services import list_blob_urls
from .services.tables_services import AzureTableService
from django.http import HttpResponseBadRequest
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
@require_http_methods(["POST", "GET"])
def create_entity_view(request):
    if request.method == 'POST':
        try:
            # Decodifica o JSON vindo no request.body
            data = json.loads(request.body)
            
            # Extrai PartitionKey e RowKey do JSON
            partition_key = data.get('PartitionKey')
            row_key = data.get('RowKey')
            
            if not partition_key or not row_key:
                return HttpResponseBadRequest("PartitionKey e RowKey são obrigatórios.")
            
            # Extrai as outras propriedades
            properties = {k: v for k, v in data.items() if k not in ['PartitionKey', 'RowKey']}
            
            # Chama o serviço para criar a entidade
            table_service.create_entity(partition_key, row_key, **properties)
            
            # Redireciona para a página de listagem após criação
            return redirect('list_entities')
        
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Erro ao decodificar o JSON.")
    
    # Se o método for GET, renderize o formulário
    return render(request, 'blobcn/create_entity.html')

# Read entity view
@require_http_methods(["GET"])
def read_entity_view(request, partition_key, row_key):
    entity = table_service.read_entity(partition_key, row_key)
    return render(request, 'blobcn/read_entity.html', {'entity': entity})

# Update entity view
@csrf_exempt
@require_http_methods(["GET", "POST"])
def update_entity_view(request, partition_key, row_key):
    if request.method == 'POST':
        try:
            # Decodifica o JSON vindo no request.body
            data = json.loads(request.body)
            print(f'POST: {data}')

            # Verifica se PartitionKey e RowKey estão presentes e corretos
            if data.get('PartitionKey') != partition_key or data.get('RowKey') != row_key:
                return HttpResponseBadRequest("PartitionKey ou RowKey inválidos.")

            # Extrai campos removidos e outras propriedades
            removed_fields = data.pop('removed_fields', [])
            properties = {k: v for k, v in data.items() if k not in ['PartitionKey', 'RowKey']}

            # Atualiza a entidade com as propriedades novas ou existentes
            table_service.update_entity(partition_key, row_key, **properties)

            # Remove os campos que foram excluídos pelo usuário
            for field in removed_fields:
                if field in table_service.read_entity(partition_key, row_key):
                    del table_service.read_entity(partition_key, row_key)[field]
            
            # Salva a entidade atualizada sem os campos removidos
            table_service.update_entity(partition_key, row_key, **table_service.read_entity(partition_key, row_key))

            return JsonResponse({'status': 'success'})  # Responde com sucesso
        
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Erro ao decodificar o JSON.")
        except Exception as e:
            print(f'Erro: {e}')
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    elif request.method == 'GET':
        try:
            # Lê a entidade com base em PartitionKey e RowKey
            entity = table_service.read_entity(partition_key, row_key)
            return render(request, 'blobcn/update_entity.html', {'entity': entity})
        except Exception as e:
            print(f'Erro ao ler entidade: {e}')
            return JsonResponse({'status': 'error', 'message': 'Erro ao ler a entidade'}, status=500)

# Delete entity view
def delete_entity_view(request, partition_key, row_key):
    table_service.delete_entity(partition_key, row_key)
    return redirect('list_entities')  # Redireciona para a página de listagem após deleção