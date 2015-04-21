'''
Created on Apr 6, 2015

@author: chris, Randy
'''

from app.database.mappers.courseMapper import CourseMapper


class Course(CourseMapper):
    
    def __init__(self,cid,name, assign_id=[], instruct_id=None):
        self.id = id
        self.name = name
        self.assign_id = assign_id
        self.instruct_id = instruct_id