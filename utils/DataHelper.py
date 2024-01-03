import json
import pandas as pd

class DataHelper:
    def __init__(self):
        """
        Initialize the DataHelper class.
        """
        pass

    def read_txt(self, path, return_type='List'):
        """
        Read data from a text file.

        Parameters:
        - path (str): The path to the text file.
        - return_type (str, optional): The desired return type ('List' or 'Str'). Default is 'List'.

        Returns:
        - list or str: The data read from the text file.

        Raises:
        - Exception: Raises an exception if an error occurs during the process.
        """
        try:
            with open(path, 'r') as file:
                if return_type == 'List':
                    return file.readlines()
                elif return_type == 'Str':
                    return file.read()
        except Exception as e:
            print(f'!ERROR! util/DataHelper.py DataHelper:read_txt():{e}')
            return None

    def write_txt(self, path, data):
        """
        Write data to a text file.

        Parameters:
        - path (str): The path to the text file.
        - data (list or str): The data to be written to the text file.

        Raises:
        - Exception: Raises an exception if an error occurs during the process.
        """
        try:
            with open(path, 'w') as file:
                file.writelines(data)
            print('Data written to text file.')
        except Exception as e:
            print(f'!ERROR! util/DataHelper.py DataHelper:write_txt():{e}')

    def read_csv(self, path, return_type='DataFrame'):
        """
        Read data from a CSV file.

        Parameters:
        - path (str): The path to the CSV file.
        - return_type (str, optional): The desired return type ('DataFrame' or 'List'). Default is 'DataFrame'.

        Returns:
        - pandas.DataFrame or list: The data read from the CSV file.

        Raises:
        - Exception: Raises an exception if an error occurs during the process.
        """
        try:
            if return_type == 'DataFrame':
                return pd.read_csv(path)
            elif return_type == 'List':
                with open(path, 'r') as file:
                    return [line.strip().split(',') for line in file.readlines()]
        except Exception as e:
            print(f'!ERROR! util/DataHelper.py DataHelper:read_csv():{e}')
            return None

    def write_csv(self, path, data):
        """
        Write data to a CSV file.

        Parameters:
        - path (str): The path to the CSV file.
        - data (pandas.DataFrame or list): The data to be written to the CSV file.

        Raises:
        - Exception: Raises an exception if an error occurs during the process.
        """
        try:
            if isinstance(data, pd.DataFrame):
                data.to_csv(path, index=False)
            elif isinstance(data, list):
                with open(path, 'w') as file:
                    for row in data:
                        file.write(','.join(map(str, row)) + '\n')
            print('Data written to CSV file.')
        except Exception as e:
            print(f'!ERROR! util/DataHelper.py DataHelper:write_csv():{e}')

    def read_json(self, path, return_type='Str'):
        """
        Read data from a JSON file.

        Parameters:
        - path (str): The path to the JSON file.
        - return_type (str, optional): The desired return type ('Str' or 'Dict'). Default is 'Str'.

        Returns:
        - str or dict: The data read from the JSON file.

        Raises:
        - Exception: Raises an exception if an error occurs during the process.
        """
        try:
            with open(path, 'r') as file:
                if return_type == 'Str':
                    return file.read()
                elif return_type == 'Dict':
                    return json.load(file)
        except Exception as e:
            print(f'!ERROR! util/DataHelper.py DataHelper.read_json():{e}')
            return None

    def write_json(self, path, data):
        """
        Write data to a JSON file.

        Parameters:
        - path (str): The path to the JSON file.
        - data (dict): The data to be written to the JSON file.

        Raises:
        - Exception: Raises an exception if an error occurs during the process.
        """
        try:
            with open(path, 'w') as file:
                if isinstance(data, dict):
                    json.dump(data, file, indent=2)
            print('Data written to JSON file.')
        except Exception as e:
            print(f'!ERROR! util/DataHelper.py DataHelper:write_json():{e}')
