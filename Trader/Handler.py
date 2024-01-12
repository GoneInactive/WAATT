import yfinance as yf

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
    MAGENTA = '\033[35m'

    LIGHT_YELLOW = '\033[93m'
    LIGHT_RED = '\033[101m'
    LIGHT_GREEN = '\033[102m'
    LIGHT_BLUE = '\033[104m'
    LIGHT_CYAN = '\033[106m'
    DARK_GRAY = '\033[90m'
    LIGHT_GRAY = '\033[37m'


class CommandHandler:
    def __init__(self):
        """Initialize the MethodHandler."""
        pass

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
        # try:
        #     # Fetch the data for the given ticker
        #     stock_data = yf.Ticker(input('Enter Ticker: '))
        #     quote = stock_data.info

        #     # Extract relevant information
        #     symbol = quote.get('symbol', 'N/A')
        #     name = quote.get('longName', 'N/A')
        #     last_price = quote.get('lastPrice', 'N/A')

        #     # Print the quote information
        #     if return_type.upper() == 'TEXT':
        #         print(f"Quote for {symbol} - {name}:")
        #         print(f"Last Price: {last_price}")
        #         return None
            
        #     return last_price

        #     # You can print more information as needed using the 'quote' dictionary

        # except Exception as e:
        #     print(f'!ERROR! Trader/Handler.py --> CommandHandler.get_quote():{e}')


if __name__ == "__main__":
    Terminal().command_line()