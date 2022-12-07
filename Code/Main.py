# These all import modules from other files which abstracts away complications.
from opener import Opener 
from sort import Sort
from save import Save

class Main(): # Creates a main class
    def __init__(self): # Initialises it
        File = input("Enter the file name to open:\n>>> ")
        openedFile = Opener(File) # These lines open then load the file
        data  = openedFile.loadFile()

        sorter = Sort(data) # This sorts  the data using the Sort method
        sorteddata = sorter.sort() # Saves this to a vatiable "sorteddata"

        saveFile = input("Enter the name of the save file:\n>>> ") # This asks what you want the save file to be called
        saver = Save(saveFile) # This uses the Save class to save the file
        saver.save(sorteddata) # This passes it the sorted data

app = Main() # Runs the Main class