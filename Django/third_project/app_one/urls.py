from django.urls import path
from app_one import views


urlpatterns = [
    path('', views.page_one, name = 'page_one')
]
