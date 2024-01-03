import os
import time
import pandas as pd
# from ..utils import DataHelper
from users.UserManager import UserManager

class DataManager:
    def __init__(self):
        self.data = None
        self.log_file_path = 'data/log/data_log.txt'

    def log_storage(self,log_data):
        """
        Log data to a log file.

        Parameters:
        - log_data (str): The data to be logged.

        Returns:
        - None: Returns None if the operation is successful.
        """
        with open('data/log/data_log.txt','w') as f:
            f.writelines(log_data)
        return None

    def store_data(self,path,data,file_exists=False):
        """
        Store data to a file.

        Parameters:
        - path (str): The file path where the data will be stored.
        - data (list): The list of data to be stored in the file.
        - file_exists (bool, optional): If True, check if the file exists before storing. Default is False.
        - admin (str, optional): The user/administrator name. Default is None.

        Returns:
        - None: Returns None if the operation is successful.

        Raises:
        - FileNotFoundError: Raises FileNotFoundError if file_exists is True and the file is not found.
        - FileExistsError: Raises FileExistsError if file_exists is False and the file already exists.
        - Exception: Raises an exception if an error occurs during the process.
        """
        if file_exists and not os.path.exists(path):
            print('!ERROR! data/DataManager DataManager:store_data(): File Not Found.')
            return None
        elif not file_exists and os.path.exists(path):
            print('!ERROR! data/DataManager DataManager:store_data(): File Already Exists')
            return None
        
        try:
            with open(path) as f:
                f.write_lines(data)
            

            self.log_storage(f'{time.time()},admin,{path}') # Time,User,Path
            print('Data Storing Done.')
            return None

        except Exception as e:
            print('!ERORR! data/DataManager DataManager.store_data():',e)

    def store_csv(self,path,df):
        """
        Store a Pandas DataFrame to a CSV file.

        Parameters:
        - path (str): The file path where the CSV file will be stored.
        - df (pd.DataFrame): The Pandas DataFrame to be stored.

        Returns:
        - None: Returns None if the operation is successful.

        Raises:
        - Exception: Raises an exception if an error occurs during the process.
        """
        try:
            df.to_csv(path, index=False)
            self.log(f'{time.time()},admin,{path}') # Time,User,Path
            print('Data Storing Done.')
            return None
        
        except Exception as e:
            print('!ERROR! data/DataManager DataManager:store_csv():',e)