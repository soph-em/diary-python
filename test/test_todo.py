from lib.todo import *
import pytest

def test_todo_initialises():
    todo = Todo("laundry")
    assert todo.todo == "laundry"
    assert todo.complete == False

def test_todo_marks_complete():
    todo1 = Todo("laundry")
    assert todo1.todo == "laundry"
    assert todo1.complete == False
    todo1.mark_complete()
    assert todo1.complete == True

def test_blank_entry():
    with pytest.raises(Exception) as e:
        todo1 = Todo("  ")
    error = str(e.value)
    assert error == 'invalid entry'

def test_wrong_type():
    with pytest.raises(Exception) as e:
        todo1 = Todo(123)
    error = str(e.value)
    assert error == 'invalid entry'