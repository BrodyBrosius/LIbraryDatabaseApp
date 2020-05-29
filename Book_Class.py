from Author_Class import *

class Book(Author):
    def __init__(self, givenAuthor,bookTitle,bookID,numOfPages,currentStatus):
        self.givenAuthor = Author()
        print(self.givenAuthor.getFirstName())
        self.bookTitle = bookTitle
        self.bookID = bookID
        self.numOfPages = numOfPages
        self.currentStatus = currentStatus

    
    def getAuthor(self):
        return self.Author

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
        
    
    def addBookToDatabase(self):
        givenBook = Book
        givenBookAuthor = givenBook.getAuthor()
        givenBookAuthorID = givenBook.getAuthor.getAuthorID()
        givenBookID = givenBook.getBookID()
        givenBookTitle = givenBook.getBookTitle()
        givenBookPages = givenBook.getNumOfPages()
        givenBookStatus = givenBook.getStatus()
        str(givenBookAuthor)
        int(givenBookAuthorID)
        int(givenBookID)
        str(givenBookTitle)
        int(givenBookPages)
        str(givenBookStatus)

        newBookConn = create_connection(r"/home/masonc/Documents/library database app/Library.db")
        newBookConn.execute("INSERT INTO BOOK (BookID,AuthorID,Title,NumOfPages,CurrentStatus)   \
                        VALUES (?,?,?,?,?)", (givenBookID, givenBookAuthorID, givenBookTitle,givenBookPages,givenBookStatus))
        newBookConn.commit()


