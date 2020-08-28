from django.urls import path
from myuser import views

urlpatterns = [
    path('', views.help, name = 'help')
]
