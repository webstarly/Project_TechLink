#!/usr/bin/python3
"""This file creates an instance of Storage. It also imports the definitions of
the BaseModel """
from models.base_model import BaseModel
from models.identity import Identity
from models.location import Location
from models.skill import Skill
from models.engine.storage import Storage

storage = Storage()
storage.reload()
