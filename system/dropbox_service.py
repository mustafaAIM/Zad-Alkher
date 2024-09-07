import dropbox
from django.conf import settings

class DropboxService:
    
    def __init__(self):
        self.dbx = dropbox.Dropbox(settings.DROPBOX_OAUTH2_TOKEN)
    
    def upload_file(self, file):
        dropbox_path = f"/planders/pdfs/{file.name}"
        try:
            self.dbx.files_upload(file.read(), dropbox_path, mode=dropbox.files.WriteMode("overwrite"))
        except dropbox.exceptions.ApiError as e:
            raise Exception(f"Dropbox API Error during upload: {str(e)}")

    def upload_and_get_link(self, file_name):
        dropbox_path = f"/planders/pdfs/{file_name}" 

        try:
            # Check if the file exists before creating a shared link
            self.dbx.files_get_metadata(dropbox_path)
            
            # Create the shared link
            shared_link_metadata = self.dbx.sharing_create_shared_link_with_settings(dropbox_path)
            shared_link_url = shared_link_metadata.url

            # Return a direct download link
            return shared_link_url.replace("?dl=0", "?dl=1")

        except dropbox.exceptions.ApiError as e:
            if isinstance(e.error, dropbox.files.GetMetadataError): 
                return f"Error: File '{dropbox_path}' not found in Dropbox."
            raise Exception(f"Dropbox API Error: {str(e)}")
