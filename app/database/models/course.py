'''
Created on Apr 6, 2015

@author: chris, Randy
'''

from app.database.mappers.courseMapper import CourseMapper


class Course(CourseMapper):
    
    def __init__(self, cid, name, descr="No Description", proj_ids=[], assign_id=[], instruct_id=None):
        self.cid = cid
        self.name = name
        self.descr = descr
        self.proj_ids = proj_ids
        self.assign_id = assign_id
        self.instruct_id = instruct_id