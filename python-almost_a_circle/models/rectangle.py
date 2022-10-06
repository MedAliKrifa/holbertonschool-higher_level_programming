
#!/usr/bin/python3
""" Rectangle """
from models.base import Base


class Rectangle(Base):
    """ class rectangle that inherits from base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ init """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """informations """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ args assign"""
        attrb = ["id", "width", "height", "x", "y"]
        if (args):
            for i in range(len(args)):
                setattr(self, attrb[i], args[i])
        else:
            for j in kwargs:
                setattr(self, j, kwargs[j])

    @property
    def width(self):
        """ width property """
        return self.__width

    @width.setter
    def width(self, w):
        """ width setter """
        if type(w) is not int:
            raise TypeError("width must be an integer")
        elif w <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = w

    @property
    def height(self):
        """ height property """
        return self.__height

    @height.setter
    def height(self, h):
        """ height setter """
        if type(h) is not int:
            raise TypeError("height must be an integer")
        elif h <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = h

    @property
    def x(self):
        """ x property """
        return self.__x

    @x.setter
    def x(self, x):
        """ x setter """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x
