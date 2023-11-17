from lib.whole_diary import *

def test_entry_adds():
    diary = Diary()
    diary.add_entry("Day 1", "Hello, Diary. Today I...")
    assert diary.diary_entries[0].title == "Day 1"
    assert diary.diary_entries[0].content == "Hello, Diary. Today I..."

def test_entry_adds_multiple():
    diary = Diary()
    diary.add_entry("Day 1", "Hello, Diary. Today I...")
    diary.add_entry("Day 2", "Hello, Diary 2. Today I...")

    assert diary.diary_entries[0].title == "Day 1"
    assert diary.diary_entries[0].content == "Hello, Diary. Today I..."    
    assert diary.diary_entries[1].title == "Day 2"
    assert diary.diary_entries[1].content == "Hello, Diary 2. Today I..."    

def test_find_entry_by_title():
    diary = Diary()
    diary.add_entry("Day 1", "Hello, Diary. Today I...")
    diary.add_entry("Day 2", "Hello, Diary 2. Today I...")

    result = diary.find_entry_by_title("Day 1")
    
    assert result == ["Hello, Diary. Today I..."]