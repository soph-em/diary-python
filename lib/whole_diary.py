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
        # for index, entry in enumerate(self.diary_entries.content):
        #     if keyword in entry:
        #         print(self.diary_entries[index].content)
                # self.search_results.append(se)

        pass # No code here yet
        #     self.search_results = []
        # for key in self.track_list:
        #     if keyword in key:
        #         self.search_results.append(f"{key} by {self.track_list[key]}")
        # return self.search_results

    def incomplete_todos():
        #list of todos with false
        pass

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
