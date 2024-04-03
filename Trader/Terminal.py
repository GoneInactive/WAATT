from Trader.Handler import CommandHandler 

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

class Terminal:
    def __init__(self):
        
        self.command_handler = CommandHandler()

        self.methods_mapping = {
            'test': self.command_handler.testing,
            'get_quote': self.command_handler.get_quote,
            'robin_trader': self.command_handler.robin_trade,
            'robin_bot': self.command_handler.robin_trade,
            'rt': self.command_handler.robin_trade,
            'restart': self.command_handler.restart_program,
            'get_price': self.command_handler.get_price,
            'get_balance': self.command_handler.get_balance,
            'get_position': self.command_handler.get_balance,
            'get_positions': self.command_handler.get_balance,
            'pos': self.command_handler.get_balance,
            'logout': self.command_handler.logout,
            'buy': self.command_handler.buy,
            'sell': self.command_handler.sell,
            'cash': self.command_handler.cash,
        }

    def command_line(self,new_window = False,cmd_running = True):
        """
        Run the main loop of the trading terminal.

        This method continuously prompts the user for input until the user types 'exit'.
        User input is processed by calling the `process_input` method.

        To exit the program, the user can type 'exit'.
        """
        print(bcolors.OKBLUE)
        if new_window:
            print('new_window mode not developed')
            raise exception('!ERROR! Trader/Terminal.py --> Terminal.command_line(): Lazy Run')
        
        else:
            while cmd_running:
                print()
                user_input = input("\nAdmin/Trader > ").strip()
                if user_input.lower() == 'exit' or user_input.lower() == 'quit':
                    print("\nExiting Trader Terminal. Goodbye!")
                    cmd_running = False
                else:
                    self.process_input(user_input)

            print(bcolors.OKCYAN)
    



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
            print('!ERROR! Trader/Terminal.py --> Terminal.process_input(): ',e)


if __name__ == "__main__":
    Terminal().command_line()