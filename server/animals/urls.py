from django.urls import path
from . import views

urlpatterns = [
    path('animals/', views.get_all_animals, name='get_all_animals'),
    path('animals/<int:animal_id>/', views.get_animal, name='get_animal'),
    path('animals/add/', views.add_animal, name='add_animal'),
]
