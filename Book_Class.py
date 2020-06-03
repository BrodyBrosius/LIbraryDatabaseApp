from Author_Class import *
import random

class Book(Author):
    def __init__(self, authorFirstName,authorLastName,authorID,bookTitle,numOfPages):
        self.authorFirstName = authorFirstName
        self.authorLastName = authorLastName
        self.authorID = authorID
        self.bookTitle = bookTitle
        self.bookID = random.randint(10000,99999)
        self.numOfPages = numOfPages
        self.currentStatus = "CHECKED IN"
        self.authorFullName = authorFirstName + " " + authorLastName

    
    def getAuthorFirstName(self):
        return self.authorFirstName
    
    def getAuthorLastName(self):
        return self.authorLastName

    def getAuthorID(self):
        return self.authorID

    def getBookTitle(self):
        return self.bookTitle
    
    def getBookID(self):
        return self.bookID

    def getNumOfPages(self):
        return self.numOfPages
    
    def getCurrentStatus(self):
        return self.currentStatus
    
    def setCurrentStatus(self,currentStatus):
        self.currentStatus = currentStatus
    
    def getAuthorFullName(self):
        return self.authorFullName
        
    
    def addBookToDatabase(self):
        newBookConn = create_connection(r"/home/masonc/Documents/library database app/Library.db")
        newBookConn.execute("INSERT INTO BOOK (BookID,AuthorID,Title,NumOfPages,CurrentStatus,AuthorFullName)   \
                            VALUES (?,?,?,?,?,?)", (int(self.getBookID()), int(self.getAuthorID()), str(self.getBookTitle()),
                            int(self.getNumOfPages()),str(self.getCurrentStatus()),str(self.getAuthorFullName())))
        newBookConn.commit()

    @staticmethod
    def displayBookTable(self):
        authConn = create_connection(r"/home/masonc/Documents/library database app/Library.db")
        cur = authConn.cursor()
        with authConn:
            cur.execute("SELECT * FROM BOOK")
            print(cur.fetchall())

