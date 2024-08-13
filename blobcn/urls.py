from django.urls import path
from . import views

urlpatterns = [
    path('storage', views.storage, name='storage'),
]