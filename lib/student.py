#!/usr/bin/env python

from user import User

class Student(User):
   
 
    def learn(self,first_name,last_name, knowledge,add_knowledge):
        super().__init__(self,first_name,last_name)
        self.knowledge = knowledge
        knowledge = []
        self.add_knowledge = add_knowledge

        knowledge.append(add_knowledge)
        