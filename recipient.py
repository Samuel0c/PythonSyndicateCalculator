
class Recipient:

    def __init__(self, name: str, account: str):
        self.name = name
        self.account = account

    # Assume that all recipients must have unique names
    def __eq__(self, obj):
        return isinstance(obj, Recipient) and obj.name == self.name
    
    def __hash__(self):
      return hash((self.name, self.account))