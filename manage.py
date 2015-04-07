#!/usr/bin/env python

'''
Created on Jun 19, 2014

@author: Chris
'''

from app import minerva

from flask_script import Manager, Shell, Server


manager = Manager(minerva)

#Used to make variables availabe to the shell if needed
def make_context():
    pass

manager.add_command('runserver', Server())
manager.add_command('shell', Shell(make_context=make_context))

if __name__ == '__main__':
    
    manager.run()