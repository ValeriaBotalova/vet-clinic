from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = "main"),
    path('appointment', views.appointment, name='appointment'),
    path('pets/', views.pet_list, name='pet_list'),
    path('pets/<int:pet_id>/', views.med_card, name='medical_card'),
]
