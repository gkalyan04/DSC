class String(object):
    def getString(self):
        self.string = input("Enter the string : ")
    def printString(self):
        print("The string is : " + self.string)
def test():
    a = String()
    a.getString()
    a.printString()
test()


