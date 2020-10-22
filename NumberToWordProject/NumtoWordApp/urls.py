from django.urls import path
from . import views

app_name = 'NumtoWordApp'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('convert/', views.convert, name = 'convert')
]
