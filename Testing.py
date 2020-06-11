from LibraryManagementConsole import *
from Author_Class import *
from Book_Class import *
from Database_Functions import *
from User_Class import *


class Test():
    def __init__(self):
        print("Testing Started...")
        newLibMgmtConsole = libraryManagementConsole(currentlyActiveUser=None)

testOne = Test()