from user import Student, Instructor
from team import Team
from assignment import Deliverable, Task
from message import TeamMessage, UserMessage
from course import Course

class CommonEqualityMixin(object):

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False
        
            
    def __ne__(self, other):
        return not self.__eq__(other)