
from product import Product
from recipient import Recipient

class Distribution:

    def __init__(self):
        self.__revenueFromProducts: dict = {}
        self.developmentFundShare: float = 0
        self.fractionToDevelopmentFund = 0.1
        self.fractionToSyndicate = 0.2

    def addProduct(self, product: Product, revenue: float, howManySold: int):
        """Add product to distribution with information about the number of sold product and total revenue obtained from sales."""
        fractionToDevelopmentFund = 0.1
        toDevelopmentFund = fractionToDevelopmentFund * revenue
        self.developmentFundShare += toDevelopmentFund
        self.__revenueFromProducts[product] = revenue - toDevelopmentFund - howManySold * product.productionPrice

    def __syndicateShare(self):
        return self.fractionToSyndicate * sum(self.__revenueFromProducts.values())
    
    def __totalAfterReductions(self, product: Product):
        return (1 - self.fractionToDevelopmentFund) * self.__revenueFromProducts[product] * (1 - self.fractionToSyndicate)
    
    def __payExcludingSyndicate(self, recipient: Recipient):
        pay: float = 0
        for product in self.__revenueFromProducts.keys():
            if recipient in product.recipients:
                pay += product.recipients[recipient] * self.__totalAfterReductions(product) / 100
        return pay
    

    def __payFromSyndicate(self, recipient: Recipient):
        pay: float = 0
        payPerMember: float = self.__syndicateShare() / len(self.__revenueFromProducts)
        for prod in self.__revenueFromProducts.keys():
            if recipient in prod.recipients:
                pay += prod.recipients[recipient] * payPerMember / 100
        return pay
    
    def pay(self, recipient: Recipient):
        """Returns the total pay to a recipient from all products of a syndicate."""
        return self.__payExcludingSyndicate(recipient) + self.__payFromSyndicate(recipient)


