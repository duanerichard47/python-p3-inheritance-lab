#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]

    def teach(self,first_name,last_name,knowledge):
        super().__init__(self,first_name,last_name)
        self.knowledge = knowledge
        return knowledge.random.randint(0,7)