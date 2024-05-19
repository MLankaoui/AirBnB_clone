#!/usr/bin/python3

# Import the custom file storage engine
from models.engine.file_storage import FileStorage

storage = FileStorage()

# Reload data from the file storage
storage.reload()
