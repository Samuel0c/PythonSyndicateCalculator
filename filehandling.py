
import re
import product
import recipient
import distribution

def readDatabase(path: str):
    """Read data from file and return a list of products."""
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

def writeResults(disr: distribution.Distribution, recipients: set, path: str = "results.txt"):
    """Write to file how much should be paid to each recipient and how much goes to development fund."""
    lines = []
    for r in recipients:
        line = " | ".join([r.name, r.account, str("%.2f" % disr.pay(r))]) + "\n"
        lines.append(line)
    f = open(path, "w")
    f.writelines(lines)
    f.write("Development fund | " + str(disr.developmentFundShare))
    f.close()


    


