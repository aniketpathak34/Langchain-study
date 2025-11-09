from typing import TypedDict


class Person(TypedDict):
    name:str
    aget:int


new_person: Person = {'name':'aniket', 'age':25}

print(new_person)