from django.urls import path
from .views import salesChart

urlpatterns = [
    path("chart/",salesChart, name="salesChart"),
]