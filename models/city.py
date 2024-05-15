#!/usr/bin/python3
"""
Defines the City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a state

    Attributes:
        name (str): The name of the state
        state_id (str): The state id

    """
    state_id: str = ""
    name: str = ""
