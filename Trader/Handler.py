from Trader.brokers.Robin_Trader import Robin_Trader
from Trader.strategies.Moving_Average import Moving_Average as MA
import sys
import os
import yfinance as yf

class bcolors:
    HEADER = '\033[95rm'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    MAGENTA = '\033[35m'
    LIGHT_YELLOW = '\033[93m'
    LIGHT_RED = '\033[101m'
    LIGHT_GREEN = '\033[102m'
    LIGHT_BLUE = '\033[104m'
    LIGHT_CYAN = '\033[106m'
    DARK_GRAY = '\033[90m'
    LIGHT_GRAY = '\033[37m'

    rt = Robin_Trader()


class CommandHandler:
    def __init__(self):
        """Initialize the MethodHandler."""
        self.rt = Robin_Trader()

    def testing(self):
        print('Trading Terminal Test Complete. 1/1 Tasks Finished.')

    def get_quote(self, return_type='PRINT'):
        try:
            ticker = input('Ticker:' )
            selected = yf.Ticker(ticker)
            finfo = selected.fast_info
            if return_type == 'PRINT':
                print(f'{bcolors.OKGREEN}{ticker}: ${round(finfo.last_price,2)} {bcolors.OKBLUE}')
            else:
                return round(finfo.last_price,2)
        except Exception as e:
            print(f'!ERROR! Trader/Handler.py --> CommandHandler.get_quote():{e}')


    def robin_trade(self):
        try:
            self.rt.test_keys()
        except Exception as e:
            print(f'!ERROR! Trader/Handler.py --> CommandHandler.rovbin_trade():{e}')

    def get_price(self):
        try:
            self.rt.get_price()
        except Exception as e:
            print(f'!ERROR! Trader/Handler.py --> CommandHandler.get_price():{e}')

    def get_balance(self):
        try:
            self.rt.get_balance()
        except Exception as e:
            print(f'!ERROR! Trader/Handler.py --> CommandHandler.get_balance():{e}')

    def logout(self):
        try:
            self.rt.log_out()
        except Exception as e:
            print(f'!ERROR! Trader/Handler.py --> CommandHandler.get_balance():{e}')

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

    def buy(self):
        self.rt.buy()

    def sell(self):
        self.rt.sell()

    def cash(self):
        self.rt.get_cash()


    def start_strategy(self):
        ### Test Robinhood Strategy
        strategy = input('Enter strategy: ')
        ma_strat = MA()
        ma_strat.run_strategy()


if __name__ == "__main__":
    Terminal().command_line()