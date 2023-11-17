class Todo():
    def __init__(self, todo):
        if type(todo) != str:
            raise Exception('invalid entry')            
        if todo.strip() == '':
            raise Exception('invalid entry')
        self.todo = todo
        self.complete = False

    def mark_complete(self):
        self.complete = True