
import re
import product
import recipient

def readDatabase(path: str):
    products = []
    with open(path, "r") as f:
        for line in f:
            if re.match(r"\S+", line):
                l = line.split("|")
                productName = l[0].strip()
                productionPrice = float(l[2].strip())
                prod = product.Product(productName, productionPrice)
                for current in l[1].split("&"):
                    cur = current.split(",")
                    recipientName = cur[0].strip()
                    recipientAccount = cur[1].strip()
                    percentage = int(cur[2].strip())
                    r = recipient.Recipient(recipientName, recipientAccount)
                    prod.addRecipient(r, percentage)
                products.append(prod)
    return products


    


