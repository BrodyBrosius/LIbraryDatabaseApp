import random
from Database_Functions import *

class Author():
    def __init__(self, passedFirstName, passedLastName):
        self.firstName = str(passedFirstName)
        self.lastName = str(passedLastName)
        self.fullName = str(passedFirstName + " " + passedLastName)
        
        exitLoop = False
        while (exitLoop == False):
            self.authorID = random.randint(1000,9999)
            if(checkIfAuthorIDAlreadyExists(authorID) == True):
                exitLoop == False
            else:
                exitLoop = True

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

    def checkIfAuthorIDAlreadyExists(self,authorID):
        authConn = create_connection(r"/home/masonc/Documents/library database app/Library.db")
        cur = authConn.cursor()
        cur.execute("SELECT * FROM AUTHOR \
                    WHERE AuthorID = ?",
                    (int(authorID)))
        result = cur.fetchone()
        if(result == None):
            return False
        else:
            return True

            

    
    def addAuthorToDatabase(self):
        newAuthConn = create_connection(r"/home/masonc/Documents/library database app/Library.db")
        cur = newAuthConn.cursor()
        print("Checking if Author is presently inside database...")
        cur.execute("SELECT * FROM AUTHOR \
                        WHERE FirstName = ?  \
                        AND LastName = ?",
                        (str(self.getFirstName()),str(self.getLastName)))
        result = cur.fetchone()
        if(result == None):
            print("Success! No conflicts detected.")
            cur.execute("INSERT INTO AUTHOR (AuthorID,FirstName,LastName,FullName)   \
                     VALUES (?,?,?,?)", (self.getAuthorID(), str(self.getFirstName()), str(self.getLastName()),str(self.getFullName())))
            newAuthConn.commit()
        else:
            print("Error! Couldnt verify author database. They may already exist in the database.")
    
    @staticmethod
    def displayAuthorTable(self):
        authConn = create_connection(r"/home/masonc/Documents/library database app/Library.db")
        cur = authConn.cursor()
        with authConn:
            cur.execute("SELECT * FROM AUTHOR")
            print(cur.fetchall())

