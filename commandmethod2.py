# The following code represents the abstract class Order and the abstract method execute():

from abc import ABCMeta, abstractmethod 

# The Command object is represented by the Order class
# Order provides you with an interface (Python's abstract base class) 
# so that
# ConcreteCommand can implement the behavior 
# The execute() method is the abstract method that needs to be defined by
# ConcreteCommand classes to execute the Order class.
# The following code represents the abstract class Order and the abstract method execute(): 

class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass 

# we have also developed certain classes that represent ConcreteCommand:
# In this case, we have two main concrete classes: BuyStockOrder and SellStockOrder
# that implement the Order interface.
# Both the ConcreteCommand classes use the object of the stock trading system
# so that they can define appropriate actions for the trading system 
# The execute() method of each of these ConcreteCommand classes uses
# the stock trade object to execute the actions to buy and sell
# Let's now look at concrete classes that implement the interface:
class BuyStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock 

    def execute(self):
        self.stock.buy() 

class SellStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock 

    def execute(self):
        self.stock.sell() 
# The StockTrade class represents the Receiver object in this example
# Receiver: This knows how to perform the operations
# associated with carrying out the request
class StockTrade:
    def __repr__(self):
        return '{}, {} perform'.format(type(self).__name__, type(self).__class__)
    def buy(self):
        print('You will buy stocks') 
    
    def sell(self):
        print('You will sell stocks')

class Agent:
    def __init__(self):
        self.__orderQueue = []        
    
    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute() 

if __name__ == '__main__':
    # Client 
    stock = StockTrade()
    buyStock = BuyStockOrder(stock) 
    sellStock = SellStockOrder(stock)        
    # Invoker 
    agent = Agent() 
    agent.placeOrder(buyStock)
    agent.placeOrder(sellStock)
