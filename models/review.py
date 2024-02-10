#!/usr/bin/python3
""" review class that inherit from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ review class """

    place_id = ""
    user_id = ""
    text = ""
