from django.urls import path
from .views import UploadFile

urlpatterns = [
    path("file/", UploadFile.as_view(), name="file")
]