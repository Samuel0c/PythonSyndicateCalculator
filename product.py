
from recipient import Recipient

class Product:

    def __init__(self, name: str, productionPrice: float):
        self.name = name
        self.productionPrice = productionPrice
        self.recipients = {}

    def addRecipient(self, recipient: Recipient, percentage: int):
        """Add recipient to the product with the percentage of contribution."""
        self.recipients[recipient] = percentage
