from AppTwo import views
from django.urls import path

urlpatterns = [
    path('', views.help, name = "help")
]
