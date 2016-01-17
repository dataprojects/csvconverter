#! /usr/bin/env python3.4
from csvconverter.filestructures import FileClass 


class FolderCleaner(): 
    """
    Removes specified files from folder
    """
    def __init__(self, folder, files):
        """
        folder - folder address where the files are located
        files - list of files        
        """
        self.folder = folder
        self.files =files
    
    def cleanDataFolder(self):
        """
        Remove the files from folder
        """                
        for file in self.files:
            FileClass(self.folder, file).file_delete()    
        print()
        print("Data directory is ready.")
 
     
