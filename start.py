from ui.CommandLine import CommandLineInterface, MethodHandler
from utils.DataHelper import DataHelper
from utils.StartUp import StartUp
from data.DataManager import DataManager
from users.UserManager import UserManager


from art import text2art


# Create an instance of the classes and run the program

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

def main():
    debug_mode = DataHelper().read_json(path='config/settings.json',return_type='Dict')['Debug-Mode']
    if debug_mode:
        print('Starting Startup Proccesses...')
    try:
        su = StartUp()
        su.log_startup()
        su.create_portfolio_files()
        if debug_mode:
            print("Task 2. Complete")
    except Exception as e:
        raise Exception(f'!ERROR! Issue during startup. Cannot Continue: {e}')

    print(bcolors.OKBLUE)
    current_version = DataHelper().read_json(path='config/settings.json',return_type='Dict')['Version']
    print(text2art(f"Welcome To"))
    print(text2art(f"WAATT"))
    print(f'{bcolors.OKGREEN}Starting Watts Accounting and Trading Tool. Running Version {current_version}...')
    print("Type 'help' for a list of commands.")

    CommandLineInterface().run()


if __name__ == "__main__":
    main()