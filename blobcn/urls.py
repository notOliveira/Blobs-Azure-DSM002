# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('storage/', views.storage, name='storage'),

    path('list-entities/', views.list_entities_view, name='list_entities'),
    path('create-entity/', views.create_entity_view, name='create_entity'),
    path('read-entity/<str:partition_key>/<str:row_key>/', views.read_entity_view, name='read_entity'),
    path('update-entity/<str:partition_key>/<str:row_key>/', views.update_entity_view, name='update_entity'),
    path('delete-entity/<str:partition_key>/<str:row_key>/', views.delete_entity_view, name='delete_entity'),
]