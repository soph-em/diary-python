from lib.diary_entry import *
import pytest

def test_diary_entry_initialises():
    entry = Diary_Entry("Title", "Dear Diary day one")
    assert entry.title == "Title"
    assert entry.content == "Dear Diary day one"

def test_todo_empty_list():
    entry = Diary_Entry("Title", "Dear Diary day one")
    assert entry.todos == []

def test_todos_blank_if_no_todos():
    entry = Diary_Entry("Title", "Dear Diary day one")
    assert entry.todos == []    

#further tests in test_integration.py due to using todo.py