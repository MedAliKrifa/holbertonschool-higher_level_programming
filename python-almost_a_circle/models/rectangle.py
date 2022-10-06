#!/usr/bin/python3
""" Rectangle """
from models.base import Base


class Rectangle(Base):
    """ class rectangle that inherits from base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialsation """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y