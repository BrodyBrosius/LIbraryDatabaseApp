import random
from Database_Functions import *
import pandas as pd

class Author():
    def __init__(self, passedFirstName, passedLastName):
        self.firstName = str(passedFirstName)
        self.lastName = str(passedLastName)
        self.fullName = str(passedFirstName + " " + passedLastName)
        self.authorID = 0
        
        exitLoop = False
        while (exitLoop == False):
            self.authorID = random.randint(1001,9999)
            if(self.checkIfAuthorIDAlreadyExists(self.authorID) == True):
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
        givenAuthorID = authorID
        authConn = create_connection(r"/home/masonc/Documents/library database app/Library.db")
        cur = authConn.cursor()
        cur.execute("SELECT * FROM AUTHOR \
                    WHERE AuthorID = ?",
                    (givenAuthorID,))
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
    def editAuthorInDatabase(AuthorID):
        inputtedID = AuthorID
        int(inputtedID)
        newAuthConn = create_connection(r"/home/masonc/Documents/library database app/Library.db")
        cur = newAuthConn.cursor()
        print("Selecting author...")
        cur.execute("SELECT * FROM AUTHOR \
                        WHERE AuthorID = ?",  \
                        (inputtedID,))
        result = cur.fetchone()
        if(result == None):
            print("Error! Could not find Author")
        else:
            print("Success! Author found!")
            print(result)
            newInput = raw_input("Is this the author entry you wanted to edit? y/n")
            if(newInput == 'y'):
                newInputTwo = raw_input("You can change the author's first or last name, which would you like to change? Input 'first' or 'last'.")
                if(newInputTwo == 'first'):
                    firstNameChange = raw_input("Please input the new first name!")
                    newAuthConn.execute("UPDATE AUTHOR \
                                SET FirstName = ? \
                                WHERE AuthorID = ?",
                                (str(firstNameChange),inputtedID))
                    newAuthConn.commit()
                elif(newInputTwo == 'last'):
                    lastNameChange = raw_input("Please input the new last name!")
                    newAuthConn.execute("UPDATE AUTHOR \
                                SET LastName = ? \
                                WHERE AuthorID = ?",
                                (str(lastNameChange),inputtedID))
                    newAuthConn.commit()
                else:
                    print("Error!")
            elif(newInput == 'n'):
                print("Exiting to main menu...")
            else:
                print("Invalid input, exiting to main menu. Remember to input exactly 'y' or 'n'. The input is case sensitive.")

    @staticmethod
    def removeAuthorFromDatabase(AuthorID):
        print("FEATURE COMING SOON") #Need more rsrch on deletion methods in SQL
    
    @staticmethod
    def displayAuthorTable(self):
        authConn = create_connection(r"/home/masonc/Documents/library database app/Library.db")
        print pd.read_sql_query("SELECT * FROM AUTHOR",authConn)

