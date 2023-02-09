#!/usr/bin/python
from models.engine import file_storage
"""create a unique FileStorage instance for the application"""


storage = file_storage.FileStorage()
storage.reload()
