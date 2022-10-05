#!/usr/bin/python3
""" class Rectangle that inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base
    """


    def __init__(self, width, height, x=0, y=0, id=None):
        """Function initialize the attributes of the class

        Parameters
        ----------
        width : int
        width of Rectangle
        height : int 
        height of Rectangle
        x : int

        y : int 

        id : int 
        id of Rectangle
        """
        id = super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
       
