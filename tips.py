def tipper():	
	bill = float(input("Please input your bill $")) 
	print ("$" + str(bill))
	percent = float(input("What percentage of tip would you like to give? "))
	tip = float((percent * .01) * bill)
	print("This is the tip amount: $" + str(float(tip)))
	total = tip + bill
	print("This is the total: $" + str(float(total)))

tipper()