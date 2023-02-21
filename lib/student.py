#!/usr/bin/env python

from user import User

class Student(User):
   
    def __(self,knowledge):
        knowledge = []
        self.knowledge = knowledge
    
    def learn(self, add_knowledge):
        knowledge = []

        knowledge.append(add_knowledge)
        