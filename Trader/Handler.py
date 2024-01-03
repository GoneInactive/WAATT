import yfinance as yf

class CommandHandler:
    def __init__(self):
        """Initialize the MethodHandler."""
        pass

    def testing(self):
        print('Trading Terminal Test Complete. 1/1 Tasks Finished.')

    def get_quote(self, return_type='Text'):
        try:
            # Fetch the data for the given ticker
            stock_data = yf.Ticker(input('Enter Ticker: '))
            quote = stock_data.info

            # Extract relevant information
            symbol = quote.get('symbol', 'N/A')
            name = quote.get('longName', 'N/A')
            last_price = quote.get('lastPrice', 'N/A')

            # Print the quote information
            if return_type.upper() == 'TEXT':
                print(f"Quote for {symbol} - {name}:")
                print(f"Last Price: {last_price}")
                return None
            
            return last_price

            # You can print more information as needed using the 'quote' dictionary

        except Exception as e:
            print(f'!ERROR! Trader/Handler.py --> CommandHandler.get_quote():{e}')


if __name__ == "__main__":
    Terminal().command_line()