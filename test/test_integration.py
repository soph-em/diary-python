from lib.diary_entry import *

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