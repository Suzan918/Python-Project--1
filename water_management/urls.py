from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('low/', views.low_list, name='low'),
    path('moderate/', views.moderate_list, name='moderate'),
    path('high/', views.high_list, name='high'),
    path('plant-search/', views.plant_search, name='plant_search'),
    path('add/', views.add_water_source, name='add'),
    path('edit/<int:pk>/', views.edit_water_source, name='edit_water_source'),
    path('delete/<int:pk>/', views.delete_water_source, name='delete_water_source'),
]
