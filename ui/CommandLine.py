import pandas as pd

import os
import sys

from users.UserManager import UserManager
from utils.DataHelper import DataHelper
from utils.StartUp import StartUp
from Portfolio.PortfolioManager import PortfolioManager

from Trader.Terminal import Terminal
from Trader.Helper import Robin_Helper

from asset_builder.asset_builder import AssetBuilder

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


pm = PortfolioManager()

class MethodHandler:
    def __init__(self):
        """Initialize the MethodHandler."""
        pass

    def reset_data(self):
        if input(f'{bcolors.WARNING}Are you sure? (Y or N)? This will ERASE all data!\n{bcolors.OKGREEN}').upper() == 'Y':
            StartUp()._delete_files()
            rh = Robin_Helper()
            rh.remove_keys()
            print('Reset Complete.')
            exit()


    def help_txt(self):
        """Implementation for method1."""
        help_commands = pd.read_csv('ui/Data/help.csv', index_col=0)
        help_commands.style.set_table_styles([{
            'selector': 'th',
            'props': [('text-align', 'left')]
        }, {
            'selector': 'td',
            'props': [('text-align', 'left')]
        }])

        # Print the styled DataFrame
        print(help_commands)
    
    
    def vers(self):
        ver = current_version = DataHelper().read_json(path='config/settings.json',return_type='Dict')['Version']
        print(f'Version: {ver}') ### It aint clean but it's honest work

    def version(self):
        """Implementation for method2."""
        print('Version Hella Beta')

    def enter_terminal(self):
        try:
            Terminal().command_line()
        except Exception as e:
            print(e)

    def restart_program(self):
        """
        Restarts the current Python script.

        This function uses os.execl to restart the script with the same Python interpreter
        and command-line arguments.

        Note: Restarting scripts is not a common practice and should be used carefully.
        """
        print('\033[0;37m!RESTARTING!')
        for _ in range(100):
            print("")
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def get_positions(self):
        pm.print_positions()


    def add_position(self):
        pm.add_position(input('Ticker: '),input('Quantity (Quantity > 0): '),input('Purchase Price ($ > 0): $'))


    def builder(self):
        AssetBuilder().__run__()
    

class CommandLineInterface:
    def __init__(self, method_handler=None):
        """
        Initialize the CommandLineInterface.

        Parameters:
            method_handler (MethodHandler): An instance of MethodHandler.
        """
        self.method_handler = MethodHandler()

        self.methods_mapping = {
            'help': self.method_handler.help_txt,
            'version': self.method_handler.vers,
            'trader': self.method_handler.enter_terminal,
            'terminal;': self.method_handler.enter_terminal,
            'trade': self.method_handler.enter_terminal,
            'reset': self.method_handler.reset_data,
            'restart': self.method_handler.restart_program,
            'positions': self.method_handler.get_positions,
            'pos': self.method_handler.get_positions,
            'add_position': self.method_handler.add_position,
            'push': self.method_handler.reset_data,
            'asset_builder': self.method_handler.builder,
        }

    def __call__(self, *args, **kwargs):
        # Code to execute when an instance is called
        print("Calling CommandLineInterface with arguments:", args)
        print("Keyword arguments:", kwargs)

    def run(self):
        """
        Run the main loop of the program.

        This method continuously prompts the user for input until the user types 'exit'.
        User input is processed by calling the `process_input` method.

        To exit the program, the user can type 'exit'.
        """
        ### 
        running = True
        while running:
            print()
            user_input = input("\nAdmin > ").strip()
            if user_input.lower() == 'exit' or user_input.lower() == 'quit':
                print("\nExiting the program. Goodbye!")
                running = False
            else:
                self.process_input(user_input)

    def process_input(self, user_input):
        """
        Process user input and execute the corresponding method.

        Parameters:
            user_input (str): The user-provided input representing a command.
        """
        try:
            method_to_execute = self.methods_mapping.get(user_input.lower())
            if callable(method_to_execute):
                method_to_execute()
            else:
                print("\nInvalid command. Try again.")

        except Exception as e:
            print('!ERROR! ui/CommandLineInterface.py --> CommandLineInterface.process_input(): ',e)


# Create an instance of the classes and run the program
if __name__ == "__main__":
    CommandLineInterface().run()
