#!/usr/bin/python3
"""This module creates the Skill class"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy import *


class Skill(BaseModel, Base):
    """A class named Skill
    Attributes:
    attr1(text): skill text
    attr2(name_id): name id associated with skill
    """
    __tablename__ = 'skill'
    text = Column(String(600), nullable=False)
    identity_id = Column(String(60), ForeignKey('identity.id'), nullable=False)
