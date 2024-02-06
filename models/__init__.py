#!/usr/bin/python3
from models.engine.file_storage import FileStorage

""" Init function to create global instances """
storage = FileStorage()
storage.reload()
