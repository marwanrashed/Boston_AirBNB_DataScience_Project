# Import nessecary packages and libararies

import pandas as pd
import numpy as np
from datetime import datetime
import re
import sklearn as sk

class HelperFunction ():

    def desired_features (self,listing_df, columns_list):
        '''
        Input: 
        listing_df: the listings dataframe for the given city.
        column_list: list of features to be removed. 
        -----------------------------------------------------
        Output:
        returns a dataframe with the desired features.
        '''
        return listing_df.drop(columns = columns_list)

    def fix_price (self,x):
        '''
        Input: price with alphanumeric and character signs. (string) 
        Output: price without any alphanumeric sign. (float)
        '''
        # if np.isnan(x): pass 
        if type(x) is str:
            trans_string = x.split('$')[1].split('.')[0]
            return    self.remove_alphanum(trans_string)
        else: pass

    def fix_rate (self,x):
        '''
        Input: rate with alphanumeric and character signs. (string) 
        Output: rate without any alphanumeric sign. (int)
        '''
        # if np.isnan(x): pass 
        if type(x) is str: return  self.remove_alphanum(x)
        else: pass

    def remove_alphanum (self,x):
        '''
        Input: string with alphanumeric and character signs. 
        Output: string without any alphanumeric sign.
        '''    
        return     re.sub(r'[^\w]','', x)
        
    def amenities_as_value (self,x):
        '''
        Input: amenities string with undesired signs
        Output: length of strings list in x . (int) 
        '''
        amenity = x.replace('{','').replace('}','').replace('"','').replace(' ','_').replace(',',' ')
        return len(amenity.split())
        
    def to_boolean (self,x):
        '''
        Input: string, t or f
        Output: int, 1 or 0
        '''    
        if x not in ['t','f'] : 
            raise Exception("Wrong entry: Not a valid boolean string")
        if x == 't': return 1
        elif x == 'f': return 0
    def weekday (self,x):
        '''
        Input: weekday number from 0 to 6. (int)
        Output: returns the corresponding day name. (string)
        '''
        week_dict = {0:'Monday', 1: 'Tuesday', 2: 'Wednesday'
        , 3: 'Thursday',4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
        if x not in week_dict.keys() : 
            raise Exception("Wrong entry: Not a weekday valid number")
        for day_num, day_name in week_dict.items(): 
            if x == day_num: return day_name
    def season (self,x):
        '''
        Input: Month of the year. (int)
        Output: season of the year (string)
        '''
        season_dict = {'Winter': [12,1,2], 'Spring': [3,4,5]
        ,'Summer': [6,7,8], 'Autumn': [9,10,11]}
        if x not in np.arange (1,13,1): 
            raise Exception("Wrong entry: Not a valid month")
        for season, months in season_dict.items(): 
            if x in months: return season