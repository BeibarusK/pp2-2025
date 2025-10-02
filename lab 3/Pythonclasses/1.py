class String:
    def __init__(self):
        self.input_str = ""

    def getString(self):
        self.input_str = input("Enter a string: ")

    def printString(self):
        print(self.input_str.upper())
s=String()
s.getString()
s.printString()