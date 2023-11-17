from lib.diary_entry import *

class Diary:

    def __init__(self):
        self.diary_entries = []
        self.todos = []
        self.contacts = []

    def add_entry(self, title, entry):
        diary_entry = Diary_Entry(title, entry)
        self.diary_entries.append(diary_entry)
        diary_entry.make_todo()
        diary_entry.make_contact()

    def find_entry_by_title(self, keyword):
        self.search_results = []
        for entry in self.diary_entries:
            if keyword in entry.title:
                self.search_results.append(entry.content)
        return self.search_results

    def incomplete_todos(self):
        self.incomplete_todos = []
        for entry in self.diary_entries:
            for todo in entry.todos:
                if todo.complete == False:
                    self.incomplete_todos.append(todo.todo)
        return self.incomplete_todos

    def complete_todos(self):
        self.complete_todos = []

        for entry in self.diary_entries:
            for todo in entry.todos:
                if todo.complete == True:
                    self.complete_todos.append(todo.todo)
        return self.complete_todos

    def best_entry_by_minutes(self, wpm, minutes):
        self.minutes_per_entry = {}

        for entry in self.diary_entries:
            total_num_words = 0
            for content in entry.content:
                words = content.split()
                num_words = len(words)
                total_num_words += num_words

            entry_minutes = total_num_words / wpm
            self.minutes_per_entry[entry_minutes] = entry.content

        self.sorted_by_minutes = dict(sorted(self.minutes_per_entry.items()))
        for minute in self.sorted_by_minutes:
            if minute > minutes:
                return self.sorted_by_minutes[minute]    

    def find_phone_numbers(self):
        self.phone_numbers = []
        for entry in self.diary_entries:
            for contact in entry.contacts:
                self.phone_numbers.append(f"{contact.name} {contact.number}")
        return self.phone_numbers

    def find_phone_number_by_name(self, search_name):
        self.phone_numbers = []
        for entry in self.diary_entries:
            for contact in entry.contacts:
                if search_name in contact.name:
                    self.phone_numbers.append(f"{contact.name} {contact.number}")
        return self.phone_numbers
