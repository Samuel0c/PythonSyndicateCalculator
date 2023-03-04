
from product import Product
from recipient import Recipient

class Distribution:

    def __init__(self):
        self.revenueFromProducts: dict = {}
        self.developmentFundShare: float = 0
        self.fractionToDevelopmentFund = 0.1
        self.fractionToSyndicate = 0.2

    def addProduct(self, product: Product, revenue: float, howManySold: int):
        fractionToDevelopmentFund = 0.1
        toDevelopmentFund = fractionToDevelopmentFund * revenue
        self.developmentFundShare += toDevelopmentFund
        self.revenueFromProducts[product] = revenue - toDevelopmentFund - howManySold * product.productionPrice

    def syndicateShare(self):
        return self.fractionToSyndicate * sum(self.revenueFromProducts.values())
    
    def totalAfterReductions(self, product: Product):
        return (1 - self.fractionToDevelopmentFund) * self.revenueFromProducts[product] * (1 - self.fractionToSyndicate)
    
    def payExcludingSyndicate(self, recipient: Recipient):
        pay: float = 0
        for product in self.revenueFromProducts.keys():
            if recipient in product.recipients:
                pay += product.recipients[recipient] * self.totalAfterReductions(product) / 100
        return pay
    

    def payFromSyndicate(self, recipient: Recipient):
        pay: float = 0
        payPerMember: float = self.syndicateShare() / len(self.revenueFromProducts)
        for prod in self.revenueFromProducts.keys():
            if recipient in prod.recipients:
                pay += prod.recipients[recipient] * payPerMember / 100
        return pay
    
    def pay(self, recipient: Recipient):
        return self.payExcludingSyndicate(recipient) + self.payFromSyndicate(recipient)


