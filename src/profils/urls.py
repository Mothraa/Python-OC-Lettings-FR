from django.urls import path
from . import views

app_name = 'profils'

urlpatterns = [
    path('', views.profiles_index, name='index'),
    path('<str:username>/', views.profile, name='profile'),
]
