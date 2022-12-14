import csv # Imports the CSV module

class Sort(): # Creates a Sort class
    '''
    This class will sort all the data into one array for the save file to use.
    '''
    def __init__(self, data): # Initialises the class
        self.data = data
        self.output_data = [] # Creates an empty output data array
        # This is the subject list - It holds all the subjects of the books in books.csv. 
        self.subject_list = ["Fiction", "fiction","Fantasy", "Drama", "Biography","Humor","Handbooks","science","Art","Biology","Economics", "Poetry","Philosophy","Political","English","French","drama","History","Bible","Classical","Mythology","Socialism","African"]
        #This is the counter list, it has one element for each subject, When one subject is mentioned, said element gains one.
        self.counter_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


    def sort(self): # creates a method "sort"
        '''
        This method will get all rows in the specified file and sorts it by seeing if the subject is in the list of subjects, then it will format it. It will save it to
        output_data

        Returns: output_data
        '''

        print("Starting sort...")

        for book in range(1, len(self.data)): # Loops over books.csv
            for subject in self.subject_list: # Looks for subjects in subject list
            
                if subject in self.data[book][2]: # If the subject is in the list
                    # print(book)
                    # print(subject)
                    # print(data[book][3])  #title
                    index = self.subject_list.index(subject) # Then get the index for the counter
                    self.counter_list[index] += 1 # Increment one to the counter
                    # Formats the row to be "('SUBEJCT_NUM', 'BOOK', 'AUTHOR', 'URL', 'YEAR')"
                    row = (subject[:3]).upper() + "_" + str(self.counter_list[index]), self.data[book][3], self.data[book][11], self.data[book][8], self.data[book][16]
                    #print(row) # Prints the rows, this is not needed for operation, only debugging
                    self.output_data.append(row) # Appends the rows to output_data
                    break
        

        print("Sort Complete..")

        return self.output_data