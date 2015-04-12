'''
Created on Apr 12, 2015

@author: chris
'''

class CommonEqualityMixin(object):
    '''
    classdocs
    '''
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False
        
            
    def __ne__(self, other):
        return not self.__eq__(other)