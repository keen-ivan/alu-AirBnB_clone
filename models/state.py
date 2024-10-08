#!/usr/bin/python3
"""Defines the State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state class with the below attribute:
        name (str): Name of the state
    """

    name = ""
