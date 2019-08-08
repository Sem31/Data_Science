# Age group
ages = []
list_of_group = []
while (True):
	age = int(input("Enter the age of the groups : "))
	if (age == 0):
		break
	elif (age < 2):
		ages.append(age)
		list_of_group.append("free admitted")
	elif (age > 3 and age <=12):
		ages.append(age)
		list_of_group.append("$14.00")
	elif (age > 12 and age <= 65):
		ages.append(age)
		list_of_group.append("$18.00")
	else :
		ages.append(age)
		list_of_group.append('$23.00')

for i in range(0,len(ages)):
	print("{} Age group cost is {}".format(ages[i],list_of_group[i]))
