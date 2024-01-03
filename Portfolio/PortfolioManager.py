import pandas as pd
import os
import yfinance as yf
import pandas as pd
import time
from utils import DataHelper

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
            # Create initial DataFrames if neither positions nor portfolio paths exist
            pos = {'Ticker': [], 'Purchase_Price': [], 'Quantity': [], 'Current_price': []}
            portfolio = {'Date': [time.time()], 'Value': [portfolio_value]}
            self.positions = pd.DataFrame(pos)
            self.portfolio_history = pd.DataFrame(portfolio)

        elif os.path.exists(self.position_path) and not os.path.exists(self.portfolio_path):
            # Raise an error if position path exists but not portfolio path
            raise Exception('!ERROR! Portfolio/PortfolioManager PortfolioManager(): Position path exists but not portfolio path')

        elif not os.path.exists(self.position_path) and os.path.exists(self.portfolio_path):
            # Raise an error if portfolio path exists but not position path
            raise Exception('!ERROR! Portfolio/PortfolioManager PortfolioManager(): Portfolio path exists but not position path')



   def positions(self):
        """
        Display the current positions.

        Returns:
        - None: Prints the positions DataFrame.

        Raises:
        - Exception: Raises an exception if there is an issue reading the positions CSV file.
        """
        try:
            positions_data = pd.read_csv('Portfolio/data/positions.csv')
            print(positions_data)
        except Exception as e:
            print(f'!ERROR! Portfolio/PortfolioManager PortfolioManager.positions(): {e}')

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
            print(f'!ERROR! Portfolio/PortfolioManager PortfolioManager.update_prices(): {e}')



    