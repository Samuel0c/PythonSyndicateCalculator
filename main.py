import filehandling
import distribution

def main():
	disr = distribution.Distribution()
	products = filehandling.readDatabase("database.txt")
	recipients = set()
	for prod in products:
		askHowMany = "How many " + prod.name + " were sold? "
		howManySold = int(input(askHowMany).strip())
		revenue: float = 0
		if howManySold > 0:
			revenue = float(input("How much revenue was obtained from this work? ").strip())
		disr.addProduct(prod, revenue, howManySold)
		for r in prod.recipients:
			recipients.add(r)

	filehandling.writeResults(disr, recipients)
	print("Results written in file results.txt!")
	
	 
if __name__ == "__main__":
	main()
	