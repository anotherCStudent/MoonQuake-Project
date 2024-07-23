from django.urls import path
from . import views
from .views import moon  # Import the new view

urlpatterns = [
    path('moon/', moon, name='moon'),
]

