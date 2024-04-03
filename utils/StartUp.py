import os
import json
import subprocess
import sys

from utils.DataHelper import DataHelper
from Trader.Helper import Robin_Helper

import robin_stocks.robinhood as rs

class StartUp:
    def __init__(self):
        """
        Initialize the StartUp class.

        Sets the path to the entries.txt file.
        """
        self.entries_file_path = 'Data/log/entries.txt'
        self.robinhood_keys_file_path = 'Data/robinhood_keys.json'
        self.debug_mode = DataHelper().read_json(path='config/settings.json',return_type='Dict')['Debug-Mode']

    def log_startup(self):
        """
        Log the program startup.

        Checks if the entries.txt file exists. If it does, reads the current value,
        increments it, and writes it back. If the file doesn't exist, creates it
        with the value 1. Prints the startup number.
        """
        # Check if the entries.txt file exists
        if os.path.exists(self.entries_file_path):
            # If the file exists, read the current value, increment it, and write it back
            with open(self.entries_file_path, 'r') as file:
                try:
                    current_value = int(file.read())
                except ValueError:
                    # Handle the case where the file contains non-integer data
                    raise Exception("Error: entries.txt contains non-integer data.")

            new_value = current_value + 1

            with open(self.entries_file_path, 'w') as file:
                file.write(str(new_value))
            if self.debug_mode:
                print(f"Program started. This is startup number: {new_value}")

        else:
            ## Program Is Starting For First Time
            with open(self.entries_file_path, 'w') as file:
                file.write('1')

            Robin_Helper().program_setup()

            print("Program started for the first time. This is startup number: 1")


    def initialize_robinhood_keys(self):
        """
        Initialize Robinhood API keys.

        Checks if it's the first program startup. If it is, prompts the user to
        enter their Robinhood API keys and stores the data in a JSON file.
        """
        return
        # if not os.path.exists(self.robinhood_keys_file_path):
        #     print("Welcome! It looks like this is the first time you're starting the program.")
        #     print("Please enter your Robinhood API keys.")

        #     # Get user input for Robinhood API keys
        #     client_id = input("Enter your Robinhood username (email): ")
        #     client_secret = input("Enter your Robinhood password: ")

        #     # Create a dictionary with the entered keys
        #     robinhood_keys = {'client_id': client_id, 'client_secret': client_secret}

        #     # Save the keys to a JSON file
        #     with open(self.robinhood_keys_file_path, 'w') as file:
        #         json.dump(robinhood_keys, file)

        #     print("Robinhood API keys have been successfully saved.")
        # else:
        #     print("Robinhood API keys are already set up.")

    def test_robinhood_keys(self):
        """
        Test if the Robinhood API keys are correct.

        If the keys are incorrect, raise an exception and delete both the
        entries.txt and robinhood_keys.json files.
        """
        return
        # if not os.path.exists(self.robinhood_keys_file_path):
        #     print("Robinhood API keys are not set up. Please run initialize_robinhood_keys first.")
        #     return

        # # Load Robinhood API keys from the JSON file
        # with open(self.robinhood_keys_file_path, 'r') as file:
        #     robinhood_keys = json.load(file)

        # rs.login(username=robinhood_keys['client_id'],
        # password=robinhood_keys['client_secret'],
        # expiresIn=86400,
        # by_sms=False)

        # print(robinhood_keys['client_id'],robinhood_keys['client_secret'])


        # print(rs.profiles.load_basic_profile())



        # print('Finished Test.')
            
        # # # If keys are incorrect, raise an exception and delete files
        # # self._delete_files()
        # # raise Exception("Invalid Robinhood API keys. Files deleted.")

    def _delete_files(self):
        """
        Delete both the entries.txt and robinhood_keys.json files.
        """
        files_to_delete = [
            self.entries_file_path,
            self.robinhood_keys_file_path,
            'Portfolio/data/positions.csv',
            'Portfolio/data/portfolio.csv',
            'Portfolio/data/trade_log.json'
        ]

        for file_path in files_to_delete:
            try:
                os.remove(file_path)
            except FileNotFoundError:
                pass

    
    def create_portfolio_files(self):
        if not os.path.exists(self.entries_file_path):
            with open('Portfolio/Data/positions.csv','w') as f:
                return
        
        return