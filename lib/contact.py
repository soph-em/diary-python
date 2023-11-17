class Contact():
    def __init__(self, name: str, number: int):
        if type(name) != str or type(number) != int:
            raise Exception("invalid data")
        if name.strip() == '' or number == None:
            raise Exception("invalid data")
        self.name = name
        self.number = number

