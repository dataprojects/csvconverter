#! /usr/bin/env python3.4
import os  
from csvconverter.cleaner import FolderCleaner    

class FileDistributor():
    """
    Distributes log file data between the files listed in data_files list.
    Each file in the data_list corresponds to the particular data type
    listed in data_types list. One file in data_files has a corresponding
    type in data_types.
    
    In other words, we want to have a separate file for each particular 
    data file instead of having all the data in one log file.
    """
    def __init__(self, data_folder, logfile_location, data_files, data_types):
        self.data_folder = data_folder
        self.logfile_location = logfile_location
        self.data_files = data_files
        self.data_types = data_types 
        
    def distribute(self):
        """
        The method distributes the logfile data accross
        the files listed in data_files list in accordance to the data type
        listed in the data_types list.   
        
        In each particular file 
        we want to have the data of one particular type     
        """
                
        # Clean data folder:
        FolderCleaner(self.data_folder, self.data_files).cleanDataFolder()
        
        print()
        print("Data distribution started...Please wait")
         
        # redistributing log file data between three data files
        # query.log, filters.log, user.log  
        with open(self.logfile_location, 'r') as f:
            for line in f:
                line = line.lstrip('I, ')
                for i in range( len(self.data_types) ):
                    if line.find( self.data_types[i] ) > -1:
                        data_file = os.path.join( self.data_folder, self.data_files[i] )
                        with open(data_file, 'a') as output_file:
                            output_file.write(line)
        print()
        print('Data distribution is over')
                             











