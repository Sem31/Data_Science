# functions 
def hello():
	print("Hello sem!")

hello()

#add two no.
def add(x,y):
	print("sum is ",(x+y))

add(5,4)

#optional parameter function
def names(name = 'sem'):
	print("name : ",name)

names("kamlesh")

#multiple parameter 
def namess(name, new_name = "prajapat"):
	print("first : "+ name +" last : "+new_name)

namess('sem','kamlesh')


# odd even check

def even(x):
	if(x%2 == 0):
		return 'even'
	else:
		return 'false'

print(even(5))

