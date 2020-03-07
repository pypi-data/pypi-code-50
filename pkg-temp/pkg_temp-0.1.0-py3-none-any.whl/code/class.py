"""
Basics to define a class
"""

# composite ####################################################
import datetime
last_id = 0
class Notebook:
    def __init__(self):
        self.notes = []

    def search(self, filter):
        return [note for note in self.notes if note.match(filter)]

    def new_note(self, memo, tags=''):
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        for note in self.notes:
            if note_id == note.id:
                note.memo = memo
                break

    def modify_tags(self, note_id, tags):
        for note in self.notes:
            if note_id == note.id:
                self.tags = tags
                break

class Note:
    def __init__(self, memo, tags):
        self.memo = memo
        self.creation_date = datetime.datetime.now()
        self.tags = tags
        global last_id
        self.id = last_id + 1

    def match(self, filter):
        return filter in self.memo or filter in self.tags


# inheritance ####################################################################
# user super with **kwargs
class Person:
    def __init__(self, age, weight, **kwargs):
        super().__init__(**kwargs)
        self.age = age
        self.weight = weight

class Child (Person):
    def __init__(self, name,  **kwargs):
        super().__init__(**kwargs)
        self.name = name

Jamy = Child('jamy', age=2, weight=7)

# use super with direct argument input
class Animal:
    def __init__(self, weight, size):
        self.weight = weight
        self.size = size

class Rabit(Animal):
    def __init__(self, weight, size, type):
        super().__init__(weight, size)
        self.type = type

rabit = Rabit(12, 1.5, 'cute')

# property decorator ###################################################################
"""
Always use a standardattribute until you need to control access to that property in some way.
Property and attribute should be noun. 
Method is just callable attribute and represent actions like a verb
"""
class User:
    def __init__(self):
        self._info = None

    @property
    def info(self):
        if not self._info:
            print('Create new info')
            self._info = 'This is new info'
        return self._info

new_user = User()
new_user.info
new_user.info


# managing objects ###########################################################
"""
Don't repeat code:
1) put repeat code as a function
2) user inheritance to create super class and have subclass override part of the method or attributes
3) User composition. just make part that are different as a new class and be included into the basic class

User manage method
1) manager method can include all the different methods to accomplish multiple tasks in a sequence
2) the detailed methods for each step in the manager method can be written separately
"""


