from lib.diary_entry import *

class Diary:

    def __init__(self):
        self.diary_entries = []
        self.todos = []
        self.contacts = []

    def add_entry(self, title, entry):
        self.diary_entries.append(Diary_Entry(title, entry))

    def find_entry_by_title(self, keyword):
        self.search_results = []
        for entry in self.diary_entries:
            if keyword in entry.title:
                self.search_results.append(entry.content)
        return self.search_results

    def incomplete_todos(self):
        self.incomplete_todos = []
        for entry in self.diary_entries:
            entry.make_todo()
            for todo in entry.todos:
                if todo.complete == False:
                    self.incomplete_todos.append(todo.todo)
        return self.incomplete_todos

    def complete_todos():
        #list of todos with true
        pass

    def best_entry_by_minutes(self,wpm,minutes):
        #reading_chunk method
        pass

    def find_phone_numbers():
        #shows list of phone numbers
        pass

    def find_phone_number_by_name(self, name):
        #input name to find phone number
        pass
