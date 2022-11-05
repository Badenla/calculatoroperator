from django.urls import path
from .views import operate

urlpatterns = [
    path('', operate, name='operate')
]