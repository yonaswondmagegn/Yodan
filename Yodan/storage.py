from django.conf import settings
from django.core.files.storage import Storage
from supabase import create_client, SupabaseStorageClient

class SupabaseStorage(Storage):
    def __init__(self, url=None, key=None, options=None, headers=None):
        self.url = url or settings.SUPABASE_URL
        self.key = key or settings.SUPABASE_ANON_KEY
        self.options = options or {}  # Additional options for SupabaseStorageClient
        self.headers = headers or {}  # Custom headers for the client

        # Ensure the key is a string
        if not isinstance(self.key, str):
            raise TypeError(f"Invalid type for key. Expected str, got {type(self.key)}: {self.key}")

        # Create the Supabase client
        supabase_client = create_client(self.url, self.key)

        # Create the SupabaseStorageClient with the Supabase client
        self.storage = SupabaseStorageClient(supabase_client, **self.options)


    def _save(self, name, content):
        # Upload the file to Supabase Storage
        self.storage.upload(name, content.read())

        # Return the name under which the file was stored
        return name
    

    def open(self, name, mode='rb'):
        # Download the file from Supabase Storage
        file_data = self.storage.download(name)

        # Return a file-like object
        return BytesIO(file_data)

    def delete(self, name):
        # Delete the file from Supabase Storage
        self.storage.remove(name)

    def exists(self, name):
        # Check if the file exists in Supabase Storage
        return self.storage.exists(name)

    def url(self, name):
        # Return the public URL of the file in Supabase Storage
        return f"{self.storage.public_url}/{name}"
