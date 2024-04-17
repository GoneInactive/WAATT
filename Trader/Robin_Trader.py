import robin_stocks.robinhood as rh
from Trader.TokenCheck import TokenCheck

import json

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

class Robin_Trader:
    def __init__(self,additional_keys=[],debug_mode=False):
        try:
            if debug_mode:
                log_pickle = input('Log Pickle? (True/False): ')
                log_pickle = bool(log_pickle)
            else:
                log_pickle = True
            base_directory = 'Trader/keys/'
            self.keys_raw = ['robin_keys_one.json']+additional_keys
            self.keys = [base_directory+key for key in self.keys_raw]
            dir = self.keys[0]
            email = 'No Input'
            password = 'No Input'
        
            with open(dir) as json_file:
                data = json.load(json_file)
                email = data['email' ]
                password = data['password']
                # print(email,password)
                rh.login(email,password,expiresIn=1000,store_session=log_pickle)
                # print('Keys are valid.')

            # rh.login(self.test_keys()[0],self.test_keys()[1])
        except Exception as e:
            print(f'!ERROR! Trader/Robin_Trader.py --> Robin_Trader.__init__():{e}')
    
    def test_keys(self,key_index=0):
        try:
            # rh.login(self.keys[key_index]['email'],self.keys[key_index]['password'])
            # rh.login(self.keys[key_index],self.keys[key_index])
            dir = self.keys[0]
            email = 'No Input'
            password = 'No Input'
        
            with open(dir) as json_file:
                data = json.load(json_file)
                email = data['email']
                password = data['password']
                rh.get_crypto_quote('BTC', 'mark_price')
                print('Keys are valid.')
            
            print(email,password)


               
        except Exception as e:
            print(f'!ERROR! Trader/Robin_Trader.py --> Robin_Trader.test_keys():{e}')
    
    def load_strategy(self,strategy):
        """
        Loads strategy i.e.
        Startegy MovingAverage.py can be loaded as load_strategy(MovingAvergae)
        """
        location = 'Trader/strategy/'+strategy+'.py'
        ### Load strategy from /strategy directory

    def get_price(self,pass_ticker=0,prnt=True):
        try:
            if pass_ticker == 0:
                ticker = input('Ticker: ')
            else:
                ticker = pass_ticker

            if list(ticker)[0] == 'c' and list(ticker)[1] == '/':
                if prnt:
                    print('Getting Crypto Price..')
                # print(ticker[-3:])
                price_btc = rh.get_crypto_quote(ticker[-3:], 'mark_price')
                # print(price_btc)
                if prnt:
                    print(f'{bcolors.OKGREEN}{ticker[-3:]}: ${round(float(price_btc),2)} {bcolors.OKBLUE}')
                return float(price_btc)
            else:
                price = rh.stocks.get_latest_price(ticker, includeExtendedHours=False)
                if prnt:
                    print(f'{bcolors.OKGREEN}{ticker}: ${round(float(price[0]),2)} {bcolors.OKBLUE}')
                return float(price[0]),2
        except Exception as e:
            print(f'!ERROR! Trader/Robin_Trader.py --> Robin_Trader.get_price():{e}')
    
    def get_balance(self):
        try:
            type = input('Type: (Crypto/Stocks): ')
            if type.upper() == 'CRYPTO':
                print('Getting Crypto Positions')
                cryptos = ['ETH','BTC','HUH']
                cryptoPos = rh.get_crypto_positions('quantity')
                # print(cryptoPos)
                for i in range(len(cryptos)):
                        print(f'{bcolors.OKGREEN+cryptos[i]}: {cryptoPos[i]}')
                
                print(bcolors.OKBLUE)

            else:
                print('Getting Stock Positions')
                # pos = rh.get_all_positions()
                pos = rh.get_open_stock_positions()
                print(pos)
        except Exception as e:
            print(f'!ERROR! Trader/Robin_Trader.py --> Robin_Trader.get_balance():{e}')
    

    def log_out(self):
        try:
            print('Logging Out.')
            rh.login('None','None',expiresIn=1000,store_session=False)
            rh.logout()
            TC = TokenCheck()
            TC.delete_file(TC.__get_token_dir())
            print('Done.')
            # exit()
        except Exception as e:
            print(f'!ERROR! Trader/Robin_Trader.py --> Robin_Trader.log_out():{e}')

    
    def buy(self):
        try:
            # order = rh.order_buy_crypto_by_price('BTC', float(input('Quantity: ')))
            order = rh.order_buy_crypto_by_price('BTC',float(input('Quantity: (in $): ')))
            print("BUY BTC AT: ${}".format(order['price']))
        except Exception as e:
            print(f'!ERROR! Trader/Robin_Trader.py --> Robin_Trader.buy():{e}')

    def sell(self):
        try:
            amt = input('Quantity: ')

            # print("POS: {}".format(position))
            order = rh.order_sell_crypto_by_quantity('BTC', amt)
            print("SELL ORDER: {}".format(order))
        except Exception as e:
            print(f'!ERROR! Trader/Robin_Trader.py --> Robin_Trader.sell():{e}')


    def get_cash(self):
        try:
            print(f"Cash: ${rh.profiles.load_account_profile()['portfolio_cash']}")
            # print(rh.profiles.load_account_profile()['portfolio_cash'])
        except Exception as e:
            print(f'!ERROR! Trader/Robin_Trader.py --> Robin_Trader.get_cash():{e}')