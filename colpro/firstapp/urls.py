
from django.urls import path
from . import views

# localhost:8000/firstapp
# localhost:8000/firstapp/order
urlpatterns = [
    path("", views.all_first, name="all_firstapp"),
]