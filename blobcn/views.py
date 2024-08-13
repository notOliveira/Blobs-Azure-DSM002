from django.shortcuts import render
from .services import list_blob_urls

# Create your views here.

def storage(request):
    # Obtenha a lista de URLs dos blobs
    blob_urls = list_blob_urls()
    
    # Renderize a view com os URLs
    return render(request, 'blobcn/storage.html', {'blob_urls': blob_urls})