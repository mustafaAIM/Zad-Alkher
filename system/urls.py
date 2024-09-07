from django.urls import path
from .views import UploadPDFView

urlpatterns = [
    path('upload-pdf/', UploadPDFView.as_view(), name='upload-pdf'),
]
