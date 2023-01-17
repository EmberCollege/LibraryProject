'''HEY WORLD'''

# These all import modules from other files which abstracts away complications.
from opener import Opener 
from sort import Sort
from save import Save

class Main(): # Creates a main class
    '''
    The class Main will instantiate all of the methods and is what makes the program work. It will open any file a user asks, then sort it, then save it in a file who's name is
    also decided by the user
    '''

    def __init__(self): # Initialises it
        ValidFile = False
        File = input("Enter the file name to open:\n>>> ")

        while ValidFile == False:

            try: 
                with open(File + ".csv", 'r', encoding='utf-8') as f:
                    openedFile = Opener(File) # These lines open then load the file
                    data  = openedFile.loadFile()

                    sorter = Sort(data) # This sorts  the data using the Sort method
                    sorteddata = sorter.sort() # Saves this to a vatiable "sorteddata"

                    saveFile = input("Enter the name of the save file:\n>>> ") # This asks what you want the save file to be called
                    saver = Save(saveFile) # This uses the Save class to save the file
                    saver.save(sorteddata) # This passes it the sorted data

                    ValidFile = True

            except:
                File = input("Please enter a valid file name: ")


app = Main() # Runs the Main class