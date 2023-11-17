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

def test_contacts_empty_list():
    entry = Diary_Entry("Title", "Dear Diary day one")
    assert entry.contacts == []    

def test_finds_and_adds_contact():
    entry = Diary_Entry("Title", "Dear Diary day one Jane: 01222 555 555")
    entry.make_contact()
    assert entry.contacts[0].number == "01222 555 555"
    assert entry.contacts[0].name == "Jane:"

def test_finds_and_adds_multiple():
    entry = Diary_Entry("Title", "Dear Diary day one Jane: 01222 555 555 Sandra: 01333 555 555")
    entry.make_contact()
    assert entry.contacts[0].number == "01222 555 555"
    assert entry.contacts[0].name == "Jane:"
    assert entry.contacts[1].number == "01333 555 555"
    assert entry.contacts[1].name == "Sandra:"