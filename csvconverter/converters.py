#! /usr/bin/env python3.4
import json
from copy import deepcopy

class Converter():
    """
    class name: Converter()
    Convert a text string to dictionary
    Suppose we are working with a structured text line,
    we want to parse the text line and save the values into dictionary
    
    Example:
    line =  'Value1 sep1 Value2 sep2 Value3'
    seplist = ['sep1', 'sep2']
    keylist = ['item1', 'item2', 'item3']
    
    by applying the converter we expect to get back
    a list containing ['Value1', 'Value2', 'Value3']
    """
    def __init__(self, line):
        
        # remove newline symbol from the text line
        line = line.rstrip('\n')
        # remove first occurence of symbols '[' and  ']'
        line = line.replace('[', '', 1)
        line = line.replace(']', '', 1)
        
        self.line = line
        
    def convertToDict(self, seplist, keylist):
        """
        See class docstring
        """
        i = 0
        ldict = dict()
        line = self.line
        for separator in seplist:
            line = line.rsplit(sep=separator, maxsplit=1)
            #print(line)
            ldict[ keylist[i] ] = str(line[0].strip())
            line = line[1]
            #print("  " + line)
            i = i+1
        ldict[ keylist[i] ] = str(line.strip())
        return ldict
        
    
class QueryLogConverter(Converter):
    """
    A special converter for query.log file
    """
    def __init__(self, line):         
        super().__init__(line)  
        self.seplist = [' #', '  INFO -- : Query: ', ', log_id: '] 
        self.keylist = ['time', 'value_id', 'query_content', 'log_id']    
        self.fieldlist = self.keylist
        
    def convert(self):
        line = super(QueryLogConverter, self).convertToDict(self.seplist, self.keylist)
        res = []
        res.append(line)
        return res      
        
    
class FiltersLogConverter(Converter):
    """
    A special converter for filters.log file
    """
    def __init__(self, line):
        super().__init__(line)
        self.seplist = [' #', '  INFO -- : Filters: ', ', log_id: ']
        self.keylist = ['time', 'value_id', 'filters', 'log_id']
        self.fieldlist = ['rid', 'time', 'value_id', 'log_id', 'filter', 'filter_value']
        
    def convert(self):
        line = super(FiltersLogConverter, self).convertToDict(self.seplist, self.keylist)
        # processing filters:
        filter_json = line['filters'].replace('=>', ': ')
        filter_dict = json.loads(filter_json)
        
        rid = 0
        res = []
        ldict = { 'log_id': line['log_id'], 
                  'time': line['time'],
                  'value_id': line['value_id'], 
                  'rid': '', 'filter':'', 'filter_value':'' }
        for key, values in filter_dict.items():
            for val in values:
                rid = rid + 1
                ldict['rid']=str(rid)
                ldict['filter'] = key
                ldict['filter_value'] = val
                res.append( deepcopy(ldict) )                                         
        return res
    
class UserLogConverter(Converter):
    """
    A special converter for user.log file
    """
    def __init__(self, line):
        """
        """
        super().__init__(line)
        self.seplist = [' #', '  INFO -- : User: ', ', log_id: ']
        self.keylist = ['time', 'value_id', 'user', 'log_id']
        
        # user dictionary structure
        self.fieldlist = ['rid', 'time', 'value_id', 'log_id', 'user_id', 'country', 'interest']
        
    def convert(self):
        """
        """ 
        # in the user.log nils are used instead of blank values
        # the program thinks that nil is a variable  
        # workaround: if nil is found insert " "
        nil = " "   
        
        line = super(UserLogConverter, self).convertToDict(self.seplist, self.keylist) 
        
        #process user data        
        rid = 0
        res = []
        user_data = eval( line['user'] )
        
        # initializing user dictionary structure
        ldict = dict( (key, '') for key in self.fieldlist )
        
        # setting user dictionary values
        ldict['time'] = line['time']
        ldict['value_id'] = line['value_id']
        ldict['log_id'] = line['log_id']                
        ldict['user_id'] = user_data[0]
        ldict['country']= user_data[1]
        
        for val in user_data[2]:
            rid = rid + 1            
            ldict['rid'] = rid
            ldict['interest'] = val
            res.append(  deepcopy(ldict) )        
        
        return res              
        
    
if __name__=='__main__':
    
    # Query log test
    line = '[2015-10-25T01:06:04.597988 #24714]  INFO -- : Query: timenote, log_id: 590ce8ea1f43'    
    print(line)    
    tst = QueryLogConverter(line).convert()
    print(tst)
    
       
    # Filter log test
    line = '[2015-10-25T12:56:08.600938 #11443]  INFO -- : Filters: {"track"=>["alpha", "beta", "start"], "parent_industry"=>["HR & Recruitment", "Sports & Fitness"]}, log_id: 03517361782c'
    tst = FiltersLogConverter(line).convert()
    print(tst)      
    
    
    # User log test
    line = '[2015-10-25T01:06:04.598323 #24714]  INFO -- : User: [526308, "Israel", ["HR & Recruitment", "Recreation & Wellness", "Big Data", "AI", "Press", "Entertainment", "Enterprise", "Philanthropy & Social Good", "UI", "UX", "AdTech", "Content & Media", "Business Intelligence", "Cloud Infrastructure", "Design", "PR", "Data Science", "Travel", "Advertising", "Sports & Fitness", "Lifestyle", "Marketing", "eCommerce", "Social Media", "Development"]], log_id: 590ce8ea1f43'
    tst = UserLogConverter(line).convert()
    for record in tst:
        print(record)
    
    
    