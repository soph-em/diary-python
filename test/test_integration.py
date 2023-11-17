from lib.diary_entry import *
from lib.whole_diary import *

def test_valid_todo_adds_object():
    entry = Diary_Entry("Title", "Dear Diary day one. #TODO laundry")
    entry.make_todo()
    assert entry.todos[0].todo == "laundry"

def test_adds_mulitple_todos():
    entry = Diary_Entry("Title", "Dear Diary day one. #TODO laundry #TODO feed pets #TODO dishwasher")
    entry.make_todo()
    assert entry.todos[0].todo == "laundry"
    assert entry.todos[1].todo == "feed pets"
    assert entry.todos[2].todo == "dishwasher"

def test_return_list_incomplete_todos():
    diary = Diary()
    diary.add_entry("Day 1", "Hello, Diary. Today I... #TODO laundry")
    diary.add_entry("Day 2", "Hello, Diary 2. Today I...")
    result = diary.incomplete_todos()
    assert result == ['laundry']

def test_return_list_complete_todos():
    diary = Diary()
    diary.add_entry("Day 1", "Hello, Diary. Today I... #TODO laundry")
    diary.add_entry("Day 2", "Hello, Diary 2. Today I...")
    result = diary.complete_todos()

    assert result == []

def test_mark_complete_and_return():
    diary = Diary()
    diary.add_entry("Day 1", "Hello, Diary. Today I... #TODO laundry")
    diary.add_entry("Day 2", "Hello, Diary 2. Today I...")

    diary.diary_entries[0].todos[0].mark_complete()
    result = diary.complete_todos()
    print(diary.diary_entries[0].todos[0].complete)
    
    assert result == ['laundry']