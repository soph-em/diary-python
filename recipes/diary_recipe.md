# Diary Multi-Class Planned Design Recipe

## 1. Describe the Problem
As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries
--Maybe just title?

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

Diary has a list of diary objects. Diary has lists of todo objects and contact objects.


Diary

diary entries []
takes diary entries objects and puts them into array

me

Diary Entry

self.content = content
self.title = title
self.todo = []
self.phone numbers = []

```
┌────────────────────────────┐
│ MusicPlayer                │
│                            │
│ - tracks                   │
│ - add(track)               │
│ - search_by_title(keyword) │
│   => [tracks...]           │
└───────────┬────────────────┘
            │
            │ owns a list of
            ▼
┌─────────────────────────┐
│ Track(title, artist)    │
│                         │
│ - title                 │
│ - artist                │
│ - format()              │
│   => "TITLE by ARTIST"  │
└─────────────────────────┘
```

_Also design the interface of each class in more detail._

```python
class Diary:

    def __init__(self):
        self.diary = []
        self.todos = []
        self.contacts = []

    def add_entry(self, entry):
        # Parameters:
        #   track: an instance of diary entry
        # Side-effects:
        #   Adds the diary entry to the diary
        pass # No code here yet

    def find_entry_by_title(self, keyword):
        # Parameters:
        #   keyword: string
        # Returns:
        #   A list of the diary objects that have titles that include the keyword
        pass # No code here yet

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

class DiaryEntry:

    def __init__(self, title, content):
        # Parameters:
        #   title: string
        #   artist: string
        """
        title
        contents
        phone numbers []
        todos []
        """
        # Side-effects:
        #   Sets the title and artist properties
        pass # No code here yet

    def find_todo(self):
        # Returns:
        #   Finds any entry with '#TODO' in it, makes it a TODO object, and puts it in the todos list.
        pass # No code here yet

    def find_phone_number():
        #Finds any numbers in diary entry and makes object.
        
class ToDo:
    def __init__(self, todo):
        self.todo = todo
        self.complete = False

    def mark_complete(self):
        self.complete = True

class Contact:
    def __init__(self, number, name):
        self.number = number
        self.name = name




```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a library
When we add two tracks
We see those tracks reflected in the tracks list
"""
library = MusicLibrary()
track_1 = Track("Carte Blanche", "Veracocha")
track_2 = Track("Synaesthesia", "The Thrillseekers")
library.add(track_1)
library.add(track_2)
library.tracks # => [track_1, track_2]
```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
- test diary entry can be added
- test diary entries can be displayed
- test diary entries can be searched by title
- test find best diary entry by minutes

- test contact can be found from diary entry
- test contact object is added to list from diary entry

- test todo can be found from diary entry
- test todo object is added to list from diary entry
- test todo object.complete is initialised as false
- test todo objec.complete can be marked as true

- test just incomplete todos can be displayed
- test just complete todos can be displayed
- test all todos can be displayed


# - test todos can be added
# - test contact can be added

"""


```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->