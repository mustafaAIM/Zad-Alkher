from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DocumentUploadSerializer
from .models import Document
from .dropbox_service import DropboxService

class UploadPDFView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = DocumentUploadSerializer(data=request.data)
        
        if serializer.is_valid(): 
            document = serializer.save()
            dropbox_service = DropboxService() 
            try:
                # Upload the file to Dropbox
                document.pdf_file.seek(0)  # Ensure file pointer is at the start
                dropbox_service.upload_file(document.pdf_file)
                
                # Get the shared link from Dropbox
                shared_link = dropbox_service.upload_and_get_link(document.pdf_file.name)
                return Response({"link": shared_link}, status=status.HTTP_201_CREATED)

            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)