import csv # Imports the CSV module

class Save(): # Creates a class called Save
    def __init__(self, saveFile): # Initialises the class
        self.saveFile = saveFile

    def save(self, output_data): # Creates a method called "save"

        print(self.saveFile)

        with open(self.saveFile + '.csv', 'w', newline='') as f: # Opens the save file and writes it, saves it in a variable called f
            f.truncate(0) # Truncates all the spaces
            writer = csv.writer(f) # Writes the file
            writer.writerow(["Code", "Tile", "Author", "URL", "Year"]) # Writes the header
            for row in output_data: 
                writer.writerow(row) # Writes all the data