# Earthquake ranges 

magnitude = float(input("Enter the magnutude : "))

if (magnitude < 2.0):
	print("the magnitude {} is considered to be a Micro earthquake.".format(magnitude))
elif (magnitude < 3.0):	
	print("the magnitude {} is considered to be a very minor earthquake.".format(magnitude))
elif (magnitude < 4.0):	
	print("the magnitude {} is considered to be a Minor earthquake.".format(magnitude))
elif (magnitude < 5.0) :	
	print("the magnitude {} is considered to be a Light earthquake.".format(magnitude))
elif (magnitude < 6.0) :	
	print("the magnitude {} is considered to be a Moderate earthquake.".format(magnitude))
elif (magnitude < 7.0) :	
	print("the magnitude {} is considered to be a Strong earthquake.".format(magnitude))
elif (magnitude < 8.0) :
	print("the magnitude {} is considered to be a Major earthquake.".format(magnitude))
elif (magnitude < 10.0):	
	print("the magnitude {} is considered to be a Great earthquake.".format(magnitude))
else :	
	print("the magnitude {} is considered to be a Meteoric earthquake.".format(magnitude))
