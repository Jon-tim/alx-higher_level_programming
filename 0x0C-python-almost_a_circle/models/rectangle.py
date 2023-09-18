#!/usr/bin/python3
"""
class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    A rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: x
            y: y
            id: id
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        # getter and setter for width
        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            """
            Args:
                value: value to be evaluated
            Exceptions:
                TypeError: if value is not an integer
                ValueError: if value is <= 0
            """
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        # getter and setter for height
        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            """
            Args:
                value: value to be evaluated
            Exceptions:
                TypeError: if value is not an integer
                ValueError: if value is <= 0
            """
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        # setter for x
        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            """
            Args:
                value: value to be evaluated
            Exceptions:
                TypeError: if value is not an integer
                ValueError: if value is < 0
            """
            if type(value) is not int:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        # setter for y
        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            """
            Args:
                value: value to be evaluated
            Exceptions:
                TypeError: if value is not an integer
                ValueError: if value is < 0
            """
            if type(value) is not int:
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

        def area(self):
            """
            Returns:
                the area of a rectangle
            """
            return self.__width * self.__height

        def display(self):
            """
            prints in stdout the Rectangle instance with the character #
            """
            for y in range(self.__y):
                print()
            for row in range(self.__height):
                for x in range(self.__x):
                    print(" ", end="")
                for col in range(self.__width):
                    print("#", end="")
                print()

        def update(self, *args, **kwargs):
            """
            assigns an argument or a key/value to each attribute
            Args:
                args: a list of arguments
                kwargs: key/value arguments
            """
            attributes = ['id', 'width', 'height', 'x', 'y']
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
                the dictionary representation of the Rectangle
            """
            return {
                    'width': self.__width,
                    'height': self.__height,
                    'x': self.__x,
                    'y': self.__y,
                    'id': self.id
                    }

        def __str__(self):
            """
            Returns:
                [Rectangle] (<id>) <x>/<y> - <width>/<height>
            """
            id = self.id
            x = self.__x
            y = self.__y
            h = self.__height
            w = self.__width
            return f"[Rectangle] ({id}) {x}/{y} - {w}/{h}"
