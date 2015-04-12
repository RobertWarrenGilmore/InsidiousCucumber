"""
Created on Apr 10, 2015

@author: chris
"""

from app.database import mongo_client

COLLECTION_NAME = 'users'

class UserMapper(object):
    
    @staticmethod
    def get_count():
        return UserMapper.get_collection().count()
    
    @staticmethod
    def get_collection():
        return mongo_client.db[COLLECTION_NAME]
    
    
    def to_hashmap(self):
        return self.__dict__


class StudentMapper(UserMapper):
    """Mapper class for students. Contains functions for database calls."""
    
    @staticmethod
    def get(query_dict):
        """Get Student based on query_dict"""
        pass
    
    @staticmethod
    def insert(student):
        """Insert a new student into the collection"""
        pass
    
    @staticmethod
    def update(query_dict, update_dict):
        pass
    
    @staticmethod
    def delete(query_dict):
        pass
    

class InstructorMapper(UserMapper):
    
    def __init__(self):
        pass