name = input("Enter the name of the month : ") 

if (name == "january" or name == "march" or name == "may" or name == "july" or name == "august" or name == "october" or name == "december"):
	print("{} is 31 days month.".format(name))
elif (name == "febuary") :
	print("{} is varies from 28 to 29 according to leap year.".format(name))
else :
	print("{} is 30 days month.".format(name))
