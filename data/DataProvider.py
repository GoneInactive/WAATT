import yfinance as yf

class DataProvider:
    def __init__(self):
        self.data = None

    def get_stock_price(self,ticker):
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
            stock = yf.Ticker(ticker)
            current_price = stock.history(period='1d')['Close'].iloc[-1]
            return current_price
        except Exception as e:
            print(f'!ERROR! data/DataProvider.py --> DataProvider.get_stock_price(): {e}')