import robin_stocks.robinhood as rh

class Robin_Trader:
    def __init__(self):
        try:
            base_directory = 'Trasder/keys/'
            self.keys = ['robin_keys_one.json']
            self.keys = ['base_directory+'+key for key in self.keys]
        except Exception as e:
            print(f'!ERROR! Trader/Robin_Trader.py --> Robin_Trader.__init__():{e}')
    
    def test_keys(self,key_index=0):
        try:
            rh.login(self.keys[key_index]['email'],self.keys[key_index]['password'])
        except Exception as e:
            print(f'!ERROR! Trader/Robin_Trader.py --> Robin_Trader.test_keys():{e}')
    
    def load_strategy(self,strategy):
        """
        Loads strategy i.e.
        Startegy MovingAverage.py can be loaded as load_strategy(MovingAvergae)
        """
        location = 'Trader/strategy/'+strategy+'.py'
        ### Load strategy from /strategy directory
    

