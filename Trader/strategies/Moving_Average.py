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

            self.prices = []
            
            self.trader = Robin_Trader()
        except Exception as e:
            print(f'!ERROR! Trader/strategy/Moving_Average.py --> Moving_Average.__init__():{e}')
        return

    
    def run_strategy(self):
        print('Starting...')
        try:
            i = 1

            while i<=20:
            #while True:
                print(i)
                if self.n_values*i >= self.average_wait_time:
                    # self.should_buy()
                    # self.should_sell()
                    pass
                if i%self.average_wait_time == 0:
                    ### Add price to moving_average
                    ma_value = self.average_value()
                else:
                    print('INFO: ',i,self.average_wait_time,i%self.average_wait_time)
                    
                time.sleep(self.price_wait_time)

                i+=1
        except Exception as e:
            print(f'!ERROR! Trader/strategy/Moving_Average.py --> Moving_Average.run_strategy():{e}')
        
    
    def should_buy(self,ma=420.69):
        print(ma,self.get_prices())
    
    def should_sell(self,ma=420.69):
        return
    
    def average_value(self):
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
            print(len(self.prices),self.n_values)
            print(f'MOVING AVERAGE: ${sum(self.prices)/self.n_values} | BTC PRICE: ${self.get_prices()}')
            return sum(self.prices)/self.n_values
        except Exception as e:
            print(f'!ERROR! Trader/strategy/Moving_Average.py --> Moving_Average.average_value():{e}')
    
    def get_prices(self):
        try:
            return self.trader.get_price(self.asset,prnt=False)
        except Exception as e:
            print(f'!ERROR! Trader/strategy/Moving_Average.py --> Moving_Average.get_prices():{e}')