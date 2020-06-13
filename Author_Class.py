import random
import pandas as pd

class Author():
    def __init__(self, passedFirstName, passedLastName):
        self.firstName = str(passedFirstName)
        self.lastName = str(passedLastName)
        self.fullName = str(passedFirstName + " " + passedLastName)
        self.authorID = random.randint(1001,9999)
    
    def getFirstName(self):
        return self.firstName
    
    def setFirstName(self, newFirstName):
        self.firstName = newFirstName
    
    def getLastName(self):
        return self.lastName

    def setLastName(self, newLastName):
        self.lastName = newLastName

    def getFullName(self):
        return self.fullName

    def getAuthorID(self):
        return self.authorID  


