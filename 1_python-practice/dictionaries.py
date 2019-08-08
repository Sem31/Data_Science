#Dictionaries programs
dict1 = {'name' : 'sem', 'age' : 21, 'addr' : 'Hyd'}
print(dict1)

#check the type
print(type(dict1))

#add the  multiple data in dictionary
dict1.update({'past':'Indore','future' : 'Hyderabad'})
print(dict1)

#keys
for keys in dict1:
	print("keys :  {0} , values : {1}".format(keys,dict1[keys]))
