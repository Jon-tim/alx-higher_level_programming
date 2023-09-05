#!/usr/bin/python3
"""A class Rectangle that defines a rectangle"""


class Rectangle:
    """A class Rectangle that defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Args:
            width: width of a rectangle
            height: height of a rectangle
        """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """property that retrieves the rectangle's width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        property that sets the rectangle's width
        Args:
            value: the given value
        Returns: the width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property that retrieves the rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        property that sets the rectangle's height
        Args:
            value: the given value
        Returns: the height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculates the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """print '#' representation of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for col in range(0, self.__height):
            for rows in range(0, self.__width):
                rect += str(self.print_symbol)
            if col is not self.__height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """Returns a representation of the rectangle"""
        class_name = type(self).__name__
        return "{}({}, {})".format(class_name, self.__width, self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        static method that compares two rectangles' area
        Args:
            rect_1: first rectangle
            rect_2: second rectangle
        Returns:
            rect_1 if greater or equal, otherwise rect_2
        Raises:
            TypeError: if rect_1 or rect_2 isn't an instance of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

    def __del__(self):
        """Detect instance deletion of rectangles"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @classmethod
    def square(cls, size=0):
        """
        class method that makes a square out of a rectangle
        Args:
            size
        Returns:
            new Rectangle instance with width == height == size
        """
        return cls(size, size)
