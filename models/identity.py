#!/usr/bin/python3
"""This module creates the Identity class"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import *


class Identity(BaseModel, Base):
    """A class that represents identity
    Attributes:
    attr1(first_name):
    attr2(last_name):
    attr3(phone_number): phone_number associated with identity
    attr4(skill): skill associated with identity
    attr5(location): location associated with identity
    """
    __tablename__ = 'identity'
    first_name = Column(String(128),nullable=False)
    last_name = Column(String(128),nullable=False)
    phone_number = Column(String(128),nullable=False)
    skill = relationship("Skill", backref="identity")
    location = relationship("Location", backref="identity")
