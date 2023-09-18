#!/usr/bin/python3
"""
a Square class that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    definition of the square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        instantiation of instance
        Args:
            size:
            x:
            y:
            id:
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        string representation
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        retrieves size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        sets size
        Args:
            value: value to be set to size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        assigns attributes
        Args:
            args: a list of arguments
            kwargs: key/value arguments
        """
        attributes = ['id', 'size', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns:
            the dictionary representation of the Square
        """
        return {
                'size': self.size,
                'x': self.x,
                'y': self.y,
                'id': self.id
                }
