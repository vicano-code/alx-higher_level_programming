#!/usr/bin/python3
"""
Module 1-Base Class

Contains a class, Base, that manages the id attribute
and a method that converts list of dictionaries to JSON
string representation
"""
import json


class Base:
    """
    manage id attribute

    methods:
    __init__(self, id=None)
    to_json_string(list_dictionaries)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initialize id attribute"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            my_json_str = []
        else:
            my_json_str = []
            for obj in list_objs:
                my_json_str.append(cls.to_dictionary(obj))
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(my_json_str))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                file_content = f.read()
        except FileNotFoundError:
            return []

        json_list = cls.from_json_string(file_content)
        list_of_instances = []
        for my_dict in json_list:
            list_of_instances.append(cls.create(**my_dict))
        return list_of_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes in CSV"""
        filename = cls.__name__ + ".csv"
        if list_objs is None:
            my_json_str = []
        else:
            my_json_str = []
            for obj in list_objs:
                my_json_str.append(cls.to_dictionary(obj))
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(my_json_str))

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                file_content = f.read()
        except FileNotFoundError:
            return []

        json_list = cls.from_json_string(file_content)
        list_of_instances = []
        for my_dict in json_list:
            list_of_instances.append(cls.create(**my_dict))
        return list_of_instances
