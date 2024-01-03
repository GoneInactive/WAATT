# from data import DataProvider
# # from strategies import MeanReversion
# # from execution import OrderManager
# # from ui.CommandLineInterface import CommandLineInterface
# # from accounting import AccountManager, TransactionManager
# # from users import UserManager

# def initialize_trading_system():
#     # Initialize data provider
#     data_provider = DataProvider()

#     # Initialize trading strategy
#     # trading_strategy = MeanReversion()

#     # Initialize order manager
#     # order_manager = OrderManager()

#     # Initialize accounting components
#     # account_manager = AccountManager()
#     # transaction_manager = TransactionManager()

#     # Initialize user management components
#     # user_manager = UserManager()
#     # user_interface = UserInterface()

#     # Startup Tasks
#     #1.0 Update Prices

#     # return data_provider, trading_strategy, order_manager, account_manager, transaction_manager, user_manager, user_interface
#     return 'Hi'

# def main():
#     # Welcome Messages

#     version = '1.0.0 BETA'

#     print(f'Starting iMAT Version {version}')


#     try:
#         ##
#         ## Startup Functions
#         ##
#         # Initialize components
#         # data_provider, trading_strategy, order_manager, account_manager, transaction_manager, user_manager, user_interface = initialize_trading_system()
#         initialize_trading_system()

#         # # Example: Fetch historical data
#         # historical_data = data_provider.fetch_historical_data('AAPL', start_date='2022-01-01', end_date='2022-12-31')

#         # # Example: Run trading strategy
#         # signals = trading_strategy.run_strategy(historical_data)

#         # # Example: Place orders
#         # orders = order_manager.execute_trading_signals(signals)

#         # # Example: Record transactions
#         # transaction_manager.record_trades(orders)

#         # # Example: Manage user accounts
#         # user_manager.create_account('John Doe')
#         # user_manager.deposit('John Doe', 10000.0)

#         # # Example: Display results in the user interface
#         # user_interface.display_results(orders)
#     except Exception as e:
#         print('!ERROR! error during startup start.py --> main(): ',e)

    

# if __name__ == "__main__":
#     main()


from ui.CommandLine import CommandLineInterface, MethodHandler
from utils.DataHelper import DataHelper
from data.DataManager import DataManager
from users.UserManager import UserManager


# Create an instance of the classes and run the program

def main():
    print(f"Starting iMAT Version {DataHelper().read_json(path='config/settings.json',return_type='Dict')['Version']}") ###
    CommandLineInterface().run()


if __name__ == "__main__":
    main()