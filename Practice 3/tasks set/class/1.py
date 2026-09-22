class string:
    def __init__(self):
        self.text=" "
    
    def getString(self):
        self.text=input("Enter a string:")
        
    def printString(self):
        print(self.text.upper())

string_handler=string()

string_handler.getString()
string_handler.printString()