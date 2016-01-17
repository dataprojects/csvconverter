import datetime

from csvconverter.distributor import FileDistributor
from csvconverter.converters import QueryLogConverter, FiltersLogConverter, UserLogConverter
from csvconverter.filestructures import FileClass, CsvFileClass
from csvconverter.csvwriter import CsvWriter

def main():
    """
    Main program: reads the data from the log/anonymised_search.log
    and creates three csv files (in the folder named data):
        query.csv: contains web site free form query data
        filters.csv: contains data about filters the users applied
            while searching the web pages
        users.csv: contains users registration data
    """
    start = datetime.datetime.now()
    # Set up
    log_folder = 'log'
    logfile_location = 'log/anonymised_search.log'
    log_files = ['query.log', 'filters.log', 'user.log']  
    data_types = ['Query', 'Filters', 'User']
    
    # csv files fieldnames
    csv_fieldnames = {}
    csv_fieldnames['query.csv'] = QueryLogConverter("").fieldlist
    csv_fieldnames['filters.csv'] = FiltersLogConverter("").fieldlist 
    csv_fieldnames['user.csv'] = UserLogConverter("").fieldlist    
        
    # Step 1: distribute the log data across three log files in the log folder:
    # query.log, filters.log, user.log    
    FileDistributor(log_folder, logfile_location, log_files, data_types).distribute() 
    
    # Step 2: write the data to csv files in the data folder:
    # query.csv, filters.csv, user.csv
        
    ## writing query.csv file
    logfile = FileClass('log/query.log')
    csvfile = CsvFileClass(csv_fieldnames['query.csv'], 'data/query.csv')
    data_type = 'Query'
    CsvWriter(logfile, csvfile, data_type).writeCsv()
    
    ## writing filters.csv file
    logfile = FileClass('log/filters.log')
    csvfile = CsvFileClass(csv_fieldnames['filters.csv'], 'data/filters.csv')
    data_type = 'Filters'
    CsvWriter(logfile, csvfile, data_type).writeCsv()
    
    ## writing user.csv file
    logfile = FileClass('log/user.log')
    csvfile = CsvFileClass(csv_fieldnames['user.csv'], 'data/user.csv')
    data_type = 'User'
    CsvWriter(logfile, csvfile, data_type).writeCsv()    
    
    # Program run time
    end = datetime.datetime.now()
    print()
    print('Program run time:', end - start, 'h:m:s.ms')
    
    
if __name__ == '__main__':
    main()
    
    