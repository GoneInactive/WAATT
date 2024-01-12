import yfinance as yf

class DataProvider:
    def __init__(self):
        self.data = None

    def get_stock_price(self,ticker,return_type='return'):
        """
        Get the most recent stock price for a given ticker.

        Parameters:
        - ticker (str): The stock ticker symbol.

        Returns:
        - float: The most recent stock price.

        Raises:
        - Exception: Raises an exception if an error occurs during the process.
         """
        try:
            selected = yf.Ticker(ticker)
            finfo = selected.fast_info
            if return_type == 'PRINT':
                print(f'{bcolors.OKGREEN}{ticker}: ${round(finfo.last_price,2)} {bcolors.OKBLUE}')
            else:
                return round(finfo.last_price,2)
        except Exception as e:
            print(f'!ERROR! data/DataProvider.py --> DataProvider.get_stock_price:{e}')

    
    def get_book(self,ticker):
        return