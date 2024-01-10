import pandas as pd
import os
import yfinance as yf
import pandas as pd
import time
import json

from utils.DataHelper import DataHelper


dh = DataHelper()

class PortfolioManager:
    def __init__(self, portfolio_value=False):
        """
        Initialize the PortfolioManager.

        Parameters:
        - portfolio_value (float, optional): Initial value for the portfolio. Default is False.

        Attributes:
        - position_path (str): The default path for the positions CSV file.
        - portfolio_path (str): The default path for the portfolio CSV file.
        - positions (pd.DataFrame): DataFrame to store position information.
        - portfolio_history (pd.DataFrame): DataFrame to store portfolio value history.

        Raises:
        - Exception: Raises an exception if there is an issue with the existence of position or portfolio paths.
        """
        self.position_path = 'Portfolio/data/positions.csv'
        self.portfolio_path = 'Portfolio/data/portfolio.csv'

        if not os.path.exists(self.position_path) and not os.path.exists(self.portfolio_path):
            print('Crating Positions and Portfolio history files.')
            # Create initial DataFrames if neither positions nor portfolio paths exist
            pos = {'Ticker': [], 'Purchase_Price': [], 'Quantity': [], 'Current_price': []}
            portfolio = {'Date': [time.time()], 'Value': [portfolio_value]}

            self.positions = pd.DataFrame(pos)
            self.portfolio_history = pd.DataFrame(portfolio)

            self.positions.to_csv(self.position_path)
            self.portfolio_history.to_csv(self.portfolio_path)

        elif os.path.exists(self.position_path) and not os.path.exists(self.portfolio_path):
            # Raise an error if position path exists but not portfolio path
            raise Exception('!ERROR! Portfolio/PortfolioManager PortfolioManager(): Position path exists but not portfolio path')

        elif not os.path.exists(self.position_path) and os.path.exists(self.portfolio_path):
            # Raise an error if portfolio path exists but not position path
            raise Exception('!ERROR! Portfolio/PortfolioManager PortfolioManager(): Portfolio path exists but not position path')
        
        # else:
        #     raise Exception(f'An unexpected error occured. Position Path: {os.path.exists(self.position_path)} | Portfolio Path: {os.path.exists(self.portfolio_path)}')




    def print_positions(self):
        print(pd.read_csv(self.position_path))

    def get_positions(self):
        """
        Display the current positions.

        Returns:
        - None: Prints the positions DataFrame.

        Raises:
        - Exception: Raises an exception if there is an issue reading the positions CSV file.
        """
        try:
            positions_data = pd.read_csv('Portfolio/data/positions.csv')
            return positions_data
        except Exception as e:
            print(f'!ERROR! Portfolio/PortfolioManager PortfolioManager.positions: {e}')

    def update_prices(self):
        """
        Update the current prices for each ticker in the positions DataFrame.

        Returns:
        - None: Updates the 'Current_price' column in the positions DataFrame.

        Raises:
        - Exception: Raises an exception if there is an issue updating the current prices.
        """
        try:
            # Read the current positions DataFrame
            positions_data = pd.read_csv(self.position_path)

            # Update the 'Current_price' column using yfinance for each ticker
            positions_data['Current_price'] = positions_data['Ticker'].apply(lambda ticker: yf.Ticker(ticker).info['lastPrice'])

            # Save the updated positions DataFrame
            positions_data.to_csv(self.position_path, index=False)

            dh.write_csv(self.position_path,positions_data)

            print('Current prices updated in the positions DataFrame.')

        except Exception as e:
            print(f'!ERROR! Portfolio/PortfolioManager PortfolioManager.update_prices: {e}')


    

    def add_position(self, ticker, quantity, purchase_price):
        """
        Add a position to the portfolio.

        Parameters:
        - ticker (str): Ticker symbol for the asset.
        - quantity (float or int): Quantity of the asset.
        - purchase_price (float or int): Purchase price of the asset.

        Example:
        >>> portfolio_manager.add_position('AAPL', 10, 150.25)
        """
        print('Does this look correct? (Y or N) ')
        print(f'Ticker: {ticker}, QTY: {quantity}, Purchase Price: ${purchase_price}')
        
        if input('> ').upper() == 'N':
            return

        quantity = float(quantity)
        purchase_price = float(purchase_price)
        
        try:
            # Retrieve the current positions DataFrame
            df = self.get_positions()

            # Prepare trade data for logging
            trade_data = {'ticker': ticker, 'quantity': quantity, 'price': purchase_price, 'timestamp': time.time()}

            # Check if the ticker already exists in the DataFrame
            if ticker in df['Ticker'].values:
                # Update the quantity and calculate the average purchase price
                existing_row = df[df['Ticker'] == ticker].iloc[0]
                existing_quantity, existing_purchase_price = existing_row['Quantity'], existing_row['Purchase_Price']
                
                new_quantity = existing_quantity + quantity
                new_purchase_price = ((existing_quantity * existing_purchase_price) + (quantity * purchase_price)) / new_quantity
                
                # Update the DataFrame with the new values
                df.loc[df['Ticker'] == ticker, ['Quantity', 'Purchase_Price']] = [new_quantity, new_purchase_price]
            else:
                # Add a new row for the new ticker
                new_row = pd.DataFrame({'Ticker': [ticker], 'Quantity': [quantity], 'Purchase_Price': [purchase_price]})
                df = df.append(new_row, ignore_index=True)

            # Save the updated DataFrame to CSV
            df.to_csv(self.position_path, index=False)
            
            # Log the trade data
            self.log_trade(trade_data)
            
            print('Done.')

        except Exception as e:
            print(f'!ERROR! Portfolio/PortfolioManager --> PortfolioManager.add_position: {e}')

    # def add_position(self, ticker, quantity, purchase_price):

    #     print('Does this look correct? (Y or N) ')
    #     print(f'Ticker: {ticker}, QTY: {quantity}, Purchase Pirce: ${purchase_price}')
    #     if input('> ') == 'N':
    #         return

    #     quantity = float(quantity)
    #     purchase_price = float(purchase_price)
    #     try:
    #         # Retrieve the current positions DataFrame
    #         df = self.get_positions()
    #         trade_data = {'ticker': ticker, 'quantity': quantity, 'price': purchase_price, 'timestamp': time.time()}

    #         # Check if the ticker already exists in the DataFrame
    #         if ticker in df['Ticker'].values:
    #             # Update the quantity and calculate the average purchase price
    #             existing_row = df[df['Ticker'] == ticker].iloc[0]
    #             existing_quantity, existing_purchase_price = existing_row['Quantity'], existing_row['Purchase_Price']
                
    #             new_quantity = existing_quantity + quantity
    #             new_purchase_price = ((existing_quantity * existing_purchase_price) + (quantity * purchase_price)) / new_quantity
                
    #             # Update the DataFrame with the new values
    #             df.loc[df['Ticker'] == ticker, ['Quantity', 'Purchase_Price']] = [new_quantity, new_purchase_price]
    #         else:
    #             # Add a new row for the new ticker
    #             new_row = pd.DataFrame({'Ticker': [ticker], 'Quantity': [quantity], 'Purchase_Price': [purchase_price]})
    #             df = df.append(new_row, ignore_index=True)

    #         # Save the updated DataFrame to CSV
    #         df.to_csv(self.position_path, index=False)
    #         self.log_trade(trade_data)
    #         print('Done.')

    #     except Exception as e:
    #         print(f'!ERROR! Portfolio/PortfolioManager --> PortfolioManager.add_position: {e}')

        
    def log_trade(self, data):
        """
        Log trade data to a text file.

        Parameters:
        - data (dict): A dictionary containing trade information.

        Example:
        >>> trade_data = {'ticker': 'AAPL', 'quantity': 10, 'price': 150.25, 'timestamp': '2022-01-08 15:30:00'}
        >>> portfolio_manager.log_trade(trade_data)
        """
        try:
            path = 'Portfolio/data/trade_log.json'

            with open(path, 'w') as f:
                # Use json.dump to write the dictionary to the file
                json.dump(data, f)
        except Exception as e:
            print(f'!ERROR! Portfolio/PortfolioManager --> PortfolioManager.log_trade: {e}')
            




