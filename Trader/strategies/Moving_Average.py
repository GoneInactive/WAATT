import pandas as pd
from Trader.brokers.Robin_Trader import Robin_Trader

import time

class Moving_Average:
    def __init__(self, wait_time=2, n_values=5, price_wait_time=1):
        ### Parameters will go here
        ### Time, asset, investment size, etc.
        try:
            self.average_wait_time = wait_time
            self.price_wait_time = price_wait_time
            self.n_values = n_values
            self.asset = "BTC"
            self.buy_size = 5.00  # amount of $ to be traded
            self.prices = []
            self.log_df = pd.DataFrame(columns=['Action', 'Price', 'Quantity', 'Moving_Average'])

            self.buy_details = {
                "has_bought": False,
                "purchase_price": 0.00,
                "purchase_quantity": 0.00,
            }

            self.trader = Robin_Trader()
        except Exception as e:
            print(f'!ERROR! Trader/strategy/Moving_Average.py --> Moving_Average.__init__():{e}')
        return

    def run_strategy(self):
        print('Starting...')
        try:
            i = 1
            debug_mode = True
            error_count = 0

            time_span = input('How long should the bot run for? (in seconds?) ')

            while i <= int(time_span):# or not debug_mode:
                print(' ')
                print(f'Iteration: {i} | Required Iterations: {self.average_wait_time * self.n_values}')
                # print(f'Has Bought? {self.buy_details['has_bought']}')
                print(f"Has Bought? {self.buy_details['has_bought']}") 
                try:
                    ma = self.average_value(print_message=False)
                    if i >= self.average_wait_time * self.n_values:
                        price = self.get_prices()
                        self.should_buy(self.trader.get_crypto_book(self.asset)['ASK'], ma)
                        self.should_sell(self.trader.get_crypto_book(self.asset)['BID'], ma)

                    # if i % self.average_wait_time == 0:
                    #     ### Add price to moving_average
                    #     ma_value = self.average_value()
                    # else:
                    #     print('INFO: ', i, self.average_wait_time, i % self.average_wait_time)
                
                except Exception as e:
                    error_count+=1
                    if debug_mode:
                        print(f'!ERROR! !ERROR DURING ITERATION! !ERROR! Trader/strategy/Moving_Average.py --> Moving_Average.run_strategy():{e}')
                        print(f'Program failed on error.')
                        i = int(time_span)

                time.sleep(self.price_wait_time)

                i += 1

            
            for i in range(40):
                print('')
            
            print(f'Finished. Errors encounted: {error_count}')
            fma = self.average_value(print_message=False)
            fprice = self.get_prices()
            self.force_sell(fma,self.trader.get_crypto_book(self.asset)['BID'])
            self.calculate_pnl()
            self.log_df.to_csv(f'Trader/Strategy_Testing/moving_average_strategy_log-{time.time()}.csv', index=False)
            print('\nLog DataFrame:')
            print(self.log_df)
            
        except Exception as e:
            print(f'!ERROR! Trader/strategy/Moving_Average.py --> Moving_Average.run_strategy():{e}')

    def should_buy(self, price, ma):
        if not self.buy_details['has_bought'] and price > ma:
            print('')
            print('')
            print(f'!!! BUY !!!')
            print(f'BOUGHT {self.buy_size / price} {self.asset} @ ${price}')
            print(price > ma)
            print(f'!!! BUY !!!')
            print('')
            print('')
            
            # Log the buy event
            # self.log_df = self.log_df.append({'Action': 'Buy', 'Price': price, 'Quantity': self.buy_size / price,
            #                                   'Moving_Average': ma}, ignore_index=True)
            self.log_df = self.log_df.append({'Action': 'Buy', 'Price': price, 'Quantity': self.buy_size / price,
                                              'Moving_Average': ma}, ignore_index=True)
            
            self.buy_details = {
                "has_bought": True,
                "purchase_price": price,
                "purchase_quantity": self.buy_size / price,
            }
            time.sleep(3)
            
    def should_sell(self, price, ma):
        if self.buy_details['has_bought'] and (price > self.buy_details['purchase_price'] * 1.001 or price < self.buy_details['purchase_price'] * 0.999):
            print('')
            print('')
            print(f'!!! SELL !!!')
            print(f"SOLD {self.buy_details['purchase_quantity']} {self.asset} @ ${price}")
            print(price < ma)
            print(f'!!! SELL !!!')
            print('')
            print('')
            
            # Log the sell event
            self.log_df = self.log_df.append({'Action': 'Sell', 'Price': price, 'Quantity': self.buy_details['purchase_quantity'],
                                              'Moving_Average': ma}, ignore_index=True)
            
            self.buy_details = {
                "has_bought": False,
                "purchase_price": 0.00,
                "purchase_quantity": 0.00,
            }
            time.sleep(1.5)

    def average_value(self, print_message=True):
        try:
            ## When called, adds price and returns the moving average price
            self.prices.append(self.get_prices())
            if len(self.prices) == self.n_values + 1:
                self.prices.pop(0)
            if print_message:
                ma = sum(self.prices) / self.n_values
                print(f'MOVING AVERAGE: ${round(sum(self.prices) / self.n_values, 2)} | BTC PRICE: ${round(self.get_prices(), 2)} | DIFF: ${self.get_prices() - round(sum(self.prices) / self.n_values, 2)}')
            return sum(self.prices) / self.n_values

        except Exception as e:
            print(f'!ERROR! Trader/strategy/Moving_Average.py --> Moving_Average.average_value():{e}')

    def get_prices(self):
        try:
            return self.trader.get_price(self.asset, prnt=False)
        except Exception as e:
            print(f'!ERROR! Trader/strategy/Moving_Average.py --> Moving_Average.get_prices():{e}')
            
    def calculate_pnl(self):
        buy_prices = self.log_df[self.log_df['Action'] == 'Buy']['Price'].values
        sell_prices = self.log_df[self.log_df['Action'] == 'Sell']['Price'].values
        buy_quantities = self.log_df[self.log_df['Action'] == 'Buy']['Quantity'].values
        sell_quantities = self.log_df[self.log_df['Action'] == 'Sell']['Quantity'].values

        buy_value = sum(buy_prices * buy_quantities)
        sell_value = sum(sell_prices * sell_quantities)

        pnl = sell_value - buy_value
        print(f'Profit/Loss: ${pnl}')

    def force_sell(self,price,ma):
        print('')
        print('')
        print(f'!!! SELL !!!')
        print(f'SOLD {self.buy_size / price} {self.asset} @ ${price}')
        print(price < ma)
        print(f'!!! SELL !!!')
        print('')
        print('')
        
        # Log the sell event
        self.log_df = self.log_df.append({'Action': 'Sell', 'Price': price, 'Quantity': self.buy_details['purchase_quantity'],
                                            'Moving_Average': ma}, ignore_index=True)
        
        self.buy_details = {
            "has_bought": False,
            "purchase_price": 0.00,
            "purchase_quantity": 0.00,
            
        }
        time.sleep(1.5)

