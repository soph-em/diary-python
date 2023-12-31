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

def test_find_phone_numbers():
    diary = Diary()
    diary.add_entry("Title", "Dear Diary day one Jane: 01222 555 555 Sandra: 01333 555 555")
    result = diary.find_phone_numbers()
    assert result == ["Jane: 01222 555 555", "Sandra: 01333 555 555"]

def test_find_phone_numbers_by_name():
    diary = Diary()
    diary.add_entry("Title", "Dear Diary day one Jane: 01222 555 555 Sandra: 01333 555 555")
    result = diary.find_phone_number_by_name("Jane")
    assert result == ["Jane: 01222 555 555"]

def test_find_best_entry():
    diary = Diary()
    diary.add_entry("Title", "Dear Diary, day 1")
    diary.add_entry("Title2", "Dear")
    diary.add_entry("Title", "Hello, world!")
    result = diary.best_entry_by_minutes(1, 1)
    assert result == "Dear"   


# def test_find_best_entry():
#     diary = Diary()
#     diary_entry1 = DiaryEntry("Title", "Dear Diary, day 1")
#     diary_entry2 = DiaryEntry("Title2", "Dear")
#     diary_entry3 = DiaryEntry("Title", "Hello, world!")

#     diary.add(diary_entry1)
#     diary.add(diary_entry2)
#     diary.add(diary_entry3)
#     result = diary.find_best_entry_for_reading_time(1, 2)
#     assert result == "Hello, world!"