from django.urls import path
from .views import SearchProductWB

urlpatterns = [
    path("search/", SearchProductWB.as_view(), name="file")
]