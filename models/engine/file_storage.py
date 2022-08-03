#!/usr/bin/env python3
'''
    Class FileStorage file.
    This class is needed to create/destroy JSON file.
'''
import json
import models


class FileStorage:
    '''
        Serializes instances to JSON file and deserializes to JSON file.
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
            This function returns the dictionary
        '''
        return (self.__objects)

    def new(self, obj):
        '''
           new(self, obj): sets in __objects, the obj with key
           <obj class name>.id
        '''
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        FileStorage.__objects[key] = obj
    
    def save(self):
        '''
            save(self): serializes __objects to the JSON
            file (path: __file_path)
        '''
        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="utf-8") as fh:
            json.dump(objects_dict, fh)

    def reload(self):
        '''
            reload(self): deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists ; otherwise, do
            nothing. If the file doesn’t exist, no exception should be raised)
        '''
        with open(FileStorage.__file_path, mode="r", encoding="utf-8") as fh:
            FileStorage.__objects = json.load(fh)
        for key, val in FileStorage.__objects.items():
            class_name = val["__class__"]
            class_name = models.classes[class_name]
            FileStorage.__objects[key] = class_name(**val)
