import json
import os

class Robin_Helper:
    def __init__(self):
        return
    
    def remove_keys(self):
        try:
           print('Removing Keys...')
           os.remove('Trader/keys/robin_keys_one.json')
           print('Done.')
        except Exception as e:
            print('!ERROR! Trader/Helper.py --> Robin_Helper.remove_keys(): ',e)
    
    def program_setup(self):
        try:
            print('Robinhood key files were not found. Would you like to set them up? (Y/N)')
            if input('/').upper() == 'Y':
                correct = False
                while not correct:
                    email = input('Email: ')
                    password = input('Password: ')
                    if input('Is this correct? (Y/N) ').upper() == 'Y':
                        correct = True
                        print('Saving Data.')
                        data = {
                            "email":email,
                            "password":password,
                            "key":"None",
                            "secret":"None"
                        }
                        with open('Trader/keys/robin_keys_one.json', 'w') as f:
                            json.dump(data, f)
                        
                        for _ in range(100):
                            print(" ")
        except Exception as e:
            print('!ERROR! Trader/Helper.py --> Robin_Helper.program_setup(): ',e)