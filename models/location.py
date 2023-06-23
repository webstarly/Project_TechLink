#!/usr/bin/python3
"""This module creates the location class"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy import *


class Location(BaseModel, Base):
    """A class named Location
    Attributes:
    attr1(text): Location text
    attr2(name_id): name id associated with Location
    """
    __tablename__ = 'Location'
    text = Column(String(600), nullable=False)
    identity_id = Column(String(60), ForeignKey('identity.id'), nullable=False)
