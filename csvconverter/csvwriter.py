#! /usr/bin/env python3.4
from csvconverter.filestructures import FileClass, CsvFileClass
from csvconverter.converters import QueryLogConverter, FiltersLogConverter, UserLogConverter

#writing query.log to query.csv

class CsvWriter():
    def __init__(self, log_file, csv_file, data_type):
        """
        log_file - FileClass object
        csv_file - CsvFileClass object
        """
        self.logfile = log_file
        self.csvfile = csv_file
        self.type = data_type
        
    def writeCsv(self):
        """
        """
        # delete csv file if it already exists  and         
        # write fieldnames into newly created csv file
        self.csvfile.write_fieldnames(delete_existing_file=True)
        
        # read log file
        with open(self.logfile.file_location, 'r') as logdata:
            # processing query log
            print('Writing data to csv file {}. Please wait...'.format(self.csvfile.file_name))            
            for line in logdata:
                if self.type == 'Query':
                    datablock = QueryLogConverter(line).convert()
                elif self.type == 'Filters':
                    datablock = FiltersLogConverter(line).convert()
                elif self.type == 'User':
                    datablock = UserLogConverter(line).convert()
                else:
                    print('Unknown data type. Use one of the following types: ')
                    print("'query', 'filter', or 'user'")
                    return                                 
 
                for dataline in datablock:
                    self.csvfile.add_line(dataline)
                    
        print('Csv file was written successfully')               
        return 1             
        

if __name__ == '__main__':
    logfile = FileClass('log/user.log')
    data_type = 'user'
    csv_fieldnames = UserLogConverter("").fieldlist
    csvfile = CsvFileClass(csv_fieldnames, 'data/user.csv')
    
    tst = CsvWriter(logfile, csvfile, data_type).writeCsv()
    print(tst)
    
    
    
    