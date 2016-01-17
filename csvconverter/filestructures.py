#! /usr/bin/env python3.4
import os 
import csv

class FileClass():
    """
    FileClass was created to simplify file handling operations
    
    class initialization:
    myFile = FileClass('folder/fileName.txt')    
    or     
    myFile = FileClass('folder', 'fileName.txt')
    
    class methods:
        add_line(): appends text line to file
        file_exists(): checks if file exists
        file_delete(): deletes the file        
    """
    def __init__(self, folder, file_name=None):
        if file_name:
            self.folder = folder
            self.file_name = file_name
            self.file_location = os.path.join(self.folder, self.file_name)
        else:
            _tmp = folder.rsplit(sep='/', maxsplit=1)
            if len(_tmp)==2:
                self.folder = _tmp[0]
                self.file_name = _tmp[1]
            elif len(_tmp)==1:
                self.folder = ''
                self.file_name = _tmp[0]
            self.file_location = folder
            _tmp = None            
        
        
    def add_line(self, line):
        """
        adds a text line to the file
        """
        with open(self.file_location, 'a') as output_file:
            output_file.write(line)
            
    def file_exists(self):
        """
        () -> int
        Checks if file exists        
        Returns 1 if file exists, and -1 otherwise
        """
        if os.path.exists(self.file_location):
            return 1
        return 0          
        
    def file_delete(self):
        """
        () -> int
        If file exsists deletes the file and returns 1
        If file does not exist returns 0
        """
        if os.path.exists(self.file_location):
            os.remove(self.file_location)
            #print('Existing file {} is deleted'.format(self.file_location))
            return 1
        #print('File {} does not exist'.format(self.file_location))
        return 0
     
class CsvFileClass(FileClass):
    """
    CsvFileClass extends the FileClass, 
    it adds the methods simplifying handling of csv files
    
    class initialization:
    myCsvFile = CsvFileClass(['field1', 'field2'], 'folder/fileName.csv')    
    or     
    myCsvFile = CsvFileClass(['field1', 'field2'], 'folder', 'fileName.csv')  
    
    class methods:
        methods inherited from FileClass
        
        write_fieldnames(): writes the fieldnames into the csv file        
    """
    def __init__(self, field_names, folder, file_name=None ):
        super().__init__(folder, file_name)
        self.field_names = field_names
        
    def add_line(self, line):
        """
        adds textline to the file
        """
        with open(self.file_location, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.field_names)
            writer.writerow( line )
        
    def write_fieldnames(self, delete_existing_file=True):
        """
        writes fieldnames to the csv file header
        """
        # if file with the same name exists delete it
        if delete_existing_file:
            self.file_delete()
        with open(self.file_location, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.field_names)
            writer.writeheader()             
            

if __name__ == '__main__':
    test1 = FileClass('media/test1.txt')
    print(test1.file_name)
    print(test1.folder)
    print(test1.file_location)
    print()
    
    test2 = FileClass('media', 'test2.txt')
    print(test2.file_name)
    print(test2.folder)
    print(test2.file_location)   
    print() 
    
    test3 = CsvFileClass(['val1', 'val2'], 'media/csvtest1.csv')
    print(test3.file_name)
    print(test3.folder)
    print(test3.file_location)
    print(test3.field_names)
    print()
    
    test4 = CsvFileClass(['val11', 'val22'], 'media', 'csvtest2.csv')
    print(test4.file_name)
    print(test4.folder)
    print(test4.file_location)
    print(test4.field_names)