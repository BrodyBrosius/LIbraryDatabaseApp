from Author_Class import *
from Book_Class import *
from Database_Functions import *
from User_Class import *
import pandas as pd
import os
import sys

class libraryManagementConsole():
    def __init__(self,currentlyActiveUser):
        

        print("Hello! Welcome to your Library Management Console! You can use this software to manage your library of books!")
        current_working_directory = os.getcwd()
        current_working_directory_and_Users_DB_file = os.path.join(current_working_directory,'Users.db')
        current_working_directory_and_Library_DB_file = os.path.join(current_working_directory, 'Library.db')
        
        if(os.path.exists(current_working_directory_and_Users_DB_file) and os.path.exists(current_working_directory_and_Library_DB_file)):
            self.createNewAccountOrLogin()

        elif(not os.path.exists(current_working_directory_and_Users_DB_file) and os.path.exists(current_working_directory_and_Library_DB_file)):
            createNewDbResponse = raw_input("There appears to be a Library Database already present but no Users database. Create one now?")
            if(createNewDbResponse == 'y'):
                self.createNewUsersDatabase()

        
        elif(os.path.exists(current_working_directory_and_Users_DB_file) and (not os.path.exists(urrent_working_directory_and_Library_DB_file))):
            createNewDbResponse = raw_input("There appears to be a Users database but no Library. Create one now?")
            if(createNewDbResponse == 'y'):
                self.createNewLibraryDatabase()

        else:
            self.createNewUsersDatabaseAndLibraryDatabase()

    def getCurrentlyActiveUser(self):
        return self.currentlyActiveUser
      

    def createNewAccountOrLogin(self):
        exitLoop = False
        isReturningUser = False
        while (exitLoop == False):
            answerOne = raw_input("Are you a new or returning user? Please input 'New' or 'Returning'\n")
            if(answerOne == 'New'):
                print("\n" + "Fantastic! Please create a new user name and password!")
                newUserName = raw_input("Username: ")
                newPassWord = raw_input("Password: ")
                isReturningUser = False
                currentNewUser = User(newUserName, newPassWord, isReturningUser)
                self.currentlyActiveUser = currentNewUser
                print(newUserName + " logged in successfully!")
                exitLoop = True
            elif(answerOne == 'Returning'):
                print("Please login!")
                oldUser = raw_input("Username: ")
                oldPassWord = raw_input("Password: ")
                self.loginUser(oldUser,oldPassWord)
                exitLoop = True
            else:
                print("\n" + "Please try again. Reminder: Input exactly either 'New' or 'Returning'.")
                exitLoop = False
            self.mainMenu()
    
    def createNewUsersDatabaseAndLibraryDatabase(self):
        createNewDbResponse = raw_input("This appears to be a new installation as no users or library databases were found. Create them now?")
        if(createNewDbResponse == 'y'):
            self.createNewUsersDatabase()            
            self.createNewLibraryDatabase()    
    
    def createNewUsersDatabase(self):
        userConn = create_connection(r"/home/masonc/Documents/library database app/Users.db")
        sql_create_users_table = """ CREATE TABLE IF NOT EXISTS USERS (
                                        UserID      INT PRIMARY KEY,
                                        UserName    TEXT,
                                        Pass        TEXT
                                    );"""
        create_table(userConn,sql_create_users_table)
        print("CONSOLE LOG: New users database and accompanying table completed.")
    
    def createNewLibraryDatabase(self):
        libConn = create_connection(r"/home/masonc/Documents/library database app/Library.db")
        sql_create_authors_table = """ CREATE TABLE IF NOT EXISTS AUTHOR (
                                        AuthorID    INT PRIMARY KEY,
                                        FirstName   VARCHAR,
                                        LastName    VARCHAR
                                    );"""
        sql_create_books_table = """CREATE TABLE IF NOT EXISTS BOOK (
                                        BookID          INT PRIMARY KEY,
                                        AuthorID        INT REFERENCES AUTHOR(AuthorID),
                                        Title           VARCHAR,
                                        NumOfPages      INT,
                                        CurrentStatus   VARCHAR,
                                        AuthorFullName  VARCHAR
                                    );"""
        create_table(libConn, sql_create_authors_table)
        create_table(libConn, sql_create_books_table)
        print("CONSOLE LOG: New Library database and accompanying tables completed.")

    def loginUser(self,userName,passWord):
            thisUserName = userName
            thisUserPassword = passWord
            loginConn = create_connection(r"/home/masonc/Documents/library database app/Users.db")
            cur = loginConn.cursor()
            cur.execute("SELECT * FROM USERS \
                        WHERE UserName = ?  \
                        AND Pass = ?", 
                        (str(thisUserName),str(thisUserPassword)))
            result = cur.fetchone()
            if(result == None):
                print("Error! User not found in database. Please create a new account or contact your systems administrator.")
            else:
                isReturning = True
                returningUser = User(thisUserName,thisUserPassword,isReturning)
                self.currentlyActiveUser = returningUser
                print("Welcome " + self.currentlyActiveUser.getUserName() + "!")

    def logoutUser(self):
        if(self.getCurrentlyActiveUser != None):
            print("Logging out " + self.getCurrentlyActiveUser().getUserName() + "...")
            self.getCurrentlyActiveUser = None
            self.createNewAccountOrLogin()
        else:
            print("Error! No user currently logged in, please login or see a systems administrator for assistance.")
            self.createNewAccountOrLogin()
    
    def mainMenu(self):
        userInput = 0
        exitLoop = False
            
        int(userInput)
        while(exitLoop == False):
            print("\n")
            print("\n ===============LIBRARY MANAGEMENT CONSOLE===============")
            print("\n Add, display, edit or remove Books from the database - 1")
            print("\n Add, or display Users from the database - 2")
            print("\n Add, display, or edit Authors from the database - 3")
            print("\n Logout - 4")
            print("\n Shutdown - 5")
            print("\n Advanced Options (Requires Admin Login) - 6") #Delete databases, may add deletion actions here as well.
            userInput = input("Please select one of the corresponding options using the number keys on your keyboard: ")

            
            #BOOK SUB-MENU
            if(userInput == 1):
                print("\n =====BOOK SUB-MENU=====")
                print("Add Book to Database (if adding a book with an author that is not in the Author table, please add the author first) - 1")
                print("Change status of a book - 2")
                print("Remove Book from Database - 3")
                print("Display all books - 4")
                bookInput = raw_input("Please select from the above options, or input 'e' to return to main menu. ")
                if(bookInput.isdigit()):
                    bookInput = int(bookInput)
                    if(bookInput == 1):
                        print("\n")
                        print("=====ADD BOOK=====")
                        authFirstName = raw_input("Author First Name: ")
                        authLastName  = raw_input("Author Last Name: ")
                        authID = raw_input("Author ID: ")
                        bookTitle = raw_input("Book Title: ")
                        numPages = input("Number of Pages: ")
                        newBook = Book(authFirstName,authLastName,authID,bookTitle,numPages)
                        newBook.addBookToDatabase()
                    elif(bookInput == 2):
                        print("\n")
                        print("=====EDIT STATUS=====")
                        Book.displayBookTable(self)
                        Book.editBookStatus(self)
                    elif(bookInput == 3):
                        print("\n")
                        print("=====REMOVE BOOK=====")
                        Book.displayBookTable(self)
                        Book.removeBookFromDatabase(self)
                    elif(bookInput == 4):
                        print("\n")
                        print("=====DISPLAYING BOOKS...=====")
                        Book.displayBookTable(self)
                        raw_input("Press any key to return to main menu")
                        self.mainMenu()
                else:
                    if(bookInput == 'e'):
                        self.mainMenu()
        #####END OF BOOK SUB-MENU#####

            #USER SUB-MENU
            elif(userInput == 2):
             print("=====USER SUB-MENU=====")
             print("\n Add new User to database - 1")
             print("\n Display all users - 2")
             thisUserInput = raw_input("\n Please select from the above options, or press 'e' to return to the main menu. ")
             if(thisUserInput.isdigit()):
                thisUserInput = int(thisUserInput)
                if(thisUserInput == 1):
                    print("\n")
                    print("=====ADD USER MENU=====")
                    newUserName = raw_input("Please enter the new user's username: ")
                    newPassWord = raw_input("Please enter the new user's password: ")
                    tempUserObj = User(newUserName,newPassWord,False)
                if(thisUserInput == 2):
                    print("\n")
                    print("=====DISPLAYING USERS...=====")
                    User.displayUserTable(self)
                    raw_input("Press any key to continue.")
                    self.mainMenu()
             else:
                self.mainMenu()

            #END OF USER SUB-MENU

            #AUTHOR SUB-MENU
            elif(userInput == 3):
                print("\n =====AUTHOR SUB-MENU=====")
                print("Add Author to Database - 1")
                print("Display Authors in Database - 2")
                print("Edit Author Currently in Database - 3")
                authInput = raw_input("Please select from the above options, or input 'e' to return to main menu. ")
                if(authInput.isdigit()):
                    authInput = int(authInput)
                    if(authInput == 1):
                        print("\n =====ADD MENU=====")
                        firstNameInput = raw_input("What is the author's first name?")
                        lastNameInput = raw_input("What is the author's last name?")
                        createdAuthor = Author(firstNameInput,lastNameInput)
                        createdAuthor.addAuthorToDatabase()
                    elif(authInput == 2):
                        Author.displayAuthorTable(self) #might want to make it prettier
                        print("\n =====EDIT MENU=====")
                        whichAuthorID = raw_input("Input the AuthorID of the Author you would like to edit.")
                        Author.editAuthorInDatabase(whichAuthorID)
                    elif(authInput == 3):
                        print("\n =====DISPLAYING AUTHORS=====")
                        Author.displayAuthorTable(self)
                        raw_input("Press any key to return to main menu")
                        self.mainMenu()
                else:
                    if(authInput == 'e'):
                        self.mainMenu()

            #END OF AUTHOR SUB-MENU
            elif(userInput == 4):
                self.logoutUser()
            elif(userInput == 5):
                print("Shutting down...")
                sys.exit()
            elif(userInput == 6):
                print("FEATURE COMING SOON")
            else:
                print("Error, unacceptable input type. Please try again.")
        







