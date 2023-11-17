from lib.todo import *
from lib.contact import *
import re

class Diary_Entry():
    def __init__(self, title, content):
        self.title = title 
        self.content = content
        self.todos = []
        self.contacts = []

    def make_todo(self):
        todos = self.content.split("#TODO")
        
        del todos[0] #removes content leaving only todos

        if "#TODO" not in self.content:
            pass

        for todo in todos:
            self.todos.append(Todo(todo.strip()))

    def make_contact(self):
        phone_regex = r"(?:(?:\(?(?:0(?:0|11)\)?[\s-]?\(?|\+)44\)?[\s-]?(?:\(?0\)?[\s-]?)?)|(?:\(?0))(?:(?:\d{5}\)?[\s-]?\d{4,5})|(?:\d{4}\)?[\s-]?(?:\d{5}|\d{3}[\s-]?\d{3}))|(?:\d{3}\)?[\s-]?\d{3}[\s-]?\d{3,4})|(?:\d{2}\)?[\s-]?\d{4}[\s-]?\d{4}))(?:[\s-]?(?:x|ext\.?|\#)\d{3,4})?"
        phone_numbers = re.findall(phone_regex, self.content)

        print(re.findall(phone_regex, self.content))
        for number in phone_numbers:
            #splits by phone number to get name which is last index of split
            before_number = self.content.split(number)
            words_before_number = before_number[0].split(' ')
            name = words_before_number[-2]
            
            self.contacts.append(Contact(name, number))




        

