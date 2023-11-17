class Contact():
    def __init__(self, name: str, number: str):
        # if type(name) != str or type(number) != str:
        #     raise Exception("invalid data")
        # if name.strip() == '' or number.strip() == '':
        #     raise Exception("invalid data")
        self.name = name
        self.number = number

