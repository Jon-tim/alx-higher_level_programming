#!/usr/bin/python3
"""
Base class definition
"""
import json


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Args:
            id (int): integer id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Args:
            list_dictionaries: a list of dictionaries
        Returns:
            the JSON string representation of list_dictionaries
            If list_dictionaries is None or empty, return the string: "[]"
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Args:
            json_string: string representing a list of dictionaries
        Returns:
            the list of the JSON string representation
            If json_string is None or empty, return an empty list
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        Args:
            list_objs: list of instances who inherits of Base
        """
        filename = f"{cls.__name__}.json"
        if list_objs is None:
            list_objs = []

        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)

        with open(filename, 'w', encoding="utf-8") as file:
            file.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Args:
            **dictionary: a double pointer to a dictionary
        Returns:
            an instance with all attributes already set
        """
        dummy_instance = cls(1, 1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Returns:
            a list of instances
        """
        pass
