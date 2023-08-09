#!/usr/bin/python3

"""
This module handles the instances of the Storage Engine
"""

import json


class FileStorage:
    """
    FileStorage class that handles read/write instances
    Attributes:
        __file_path (file): file to work with
        __objects (obj): Json Object
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return dictionary __objects with no specifics
        Return:
            Brings all the objects in storage
        """
        return self.__objects

    def new(self, obj):
        """
        Creates a new object with key
        Args:
            self: self
            obj (obj): The object to work with
        """
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[obj_key] = obj

    def save(self):
        """
        Saves the object blob to File Storage
        new_obj is a dictionary format for the object storage
        """
        new_obj = {key: values.to_dict() for key, values in self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf8") as file:
            file.write(json.dumps(new_obj))

    def reload(self):
        """
        This loads objects from the specified file.
        If not present still pass the function
        """
        from models.base_model import BaseModel

        # NOTE: Bring the BaseModel for easy retrieval
        class_dict = {"BaseModel": BaseModel}

        try:
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
                for value in self.__objects.values():
                    class_name = value["__class__"]
                    del value["__class__"]
                    if class_name in class_dict:
                        self.new(class_dict[class_name](**value))
        except FileNotFoundError:
            pass

        return self.__objects
