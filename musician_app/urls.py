from django.urls import path
from .import views

urlpatterns = [
    path('add/',views.add_music,name='add_music'),
    path('edit/<str:first_name>/<str:last_name>/',views.edit_music,name='edit_music'),
]
