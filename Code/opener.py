import csv # Import the CSV module

class Opener(): # Creates an Opener class
    '''
    Opens the file, creating a data array. It also accepts the file name the user inputted.
    '''
    def __init__(self,file: str) -> list: # Initialises the class
        self.file = file 
        self.data = [] # Creates a data array

    def loadFile(self): # Creates a method called "loadFile"
        '''
        This loads the file to read, and appends it to the data array.

        Returns: self.data
        '''
        with open(self.file + ".csv", 'r', encoding='utf-8') as f: # Opens the file in read mode - saves it in a variable f
            bookdata = csv.reader(f) # Reads the file
            for row in bookdata:
                self.data.append(row) # Makes into a list of data for the sorter to use

        return self.data

# Stupid