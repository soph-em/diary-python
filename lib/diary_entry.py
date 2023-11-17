from lib.todo import *

class Diary_Entry():
    def __init__(self, title, content):
        self.title = title 
        self.content = content
        self.todos = []

    def make_todo(self):
        todos = self.content.split("#TODO")
        
        del todos[0] #removes content leaving only todos

        if "#TODO" not in self.content:
            pass

        for todo in todos:
            self.todos.append(Todo(todo.strip()))



