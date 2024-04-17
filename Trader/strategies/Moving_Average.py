from Trader.Robin_Trader import Robin_Trader

import time

class Moving_Average:
    def __init__(self,wait_time=1,n_values=10,price_wait_time=1):
        ### Parameters will go here
        ### Time, asset, investment size, etc.
        try:
            self.average_wait_time=wait_time
            self.price_wait_time=price_wait_time
            self.n_values = n_values
            self.asset = "c/BTC"
            self.buy_size = 5.00 ### amount of $ to be traded

            self.prices = []
            
            self.trader = Robin_Trader()
        except Exception as e:
            print(f'!ERROR! Trader/strategy/Moving_Average.py --> Moving_Average.__init__():{e}')
        return

    
    def run_strategy(self):
        print('Starting...')
        try:
            i = 1
            debug_mode = True

            while i<=20 or not debug_mode:
            #while True:
                print(' ')
                print(f'Iteration: {i} | Required Iterations: {self.average_wait_time*self.n_values}')
                if i>=self.average_wait_time*self.n_values:
                    ma = self.average_value(print_message=False)
                    price = self.get_prices()
                    self.should_buy(price,ma)
                    self.should_sell(price,ma)

                if i%self.average_wait_time == 0:
                    ### Add price to moving_average
                    ma_value = self.average_value()
                else:
                    print('INFO: ',i,self.average_wait_time,i%self.average_wait_time)
                    
                time.sleep(self.price_wait_time)

                i+=1
        except Exception as e:
            print(f'!ERROR! Trader/strategy/Moving_Average.py --> Moving_Average.run_strategy():{e}')
        
    
    def should_buy(self,price,ma):
        current_position = 0
        if current_position == 0:
            if price > ma:
                print('')
                print('')
                print(f'!!! BUY !!!')
                print(f'BOUGHT {self.buy_size/price} of {self.asset} at ${self.buy_size*price}')
                print(f'!!! BUY !!!')
                print('')
                print('')
                time.sleep(3)
    def should_sell(self,price,ma):
        return
    
    def average_value(self,print_message=True):
        try:
            ## When called, adds price and returns the moving average price 
            self.prices.append(self.get_prices())
            # print('GET_PRICES, PRICES, self.prices')
            # print(self.get_prices())
            # print(self.prices)
            # print(type(self.prices))
            # exit()
            if len(self.prices) == self.n_values+1:
                self.prices.pop(0)
            if print_message:
                print(f'MOVING AVERAGE: ${sum(self.prices)/self.n_values} | BTC PRICE: ${self.get_prices()}')
            return sum(self.prices)/self.n_values
        except Exception as e:
            print(f'!ERROR! Trader/strategy/Moving_Average.py --> Moving_Average.average_value():{e}')
    
    def get_prices(self):
        try:
            return self.trader.get_price(self.asset,prnt=False)
        except Exception as e:
            print(f'!ERROR! Trader/strategy/Moving_Average.py --> Moving_Average.get_prices():{e}')