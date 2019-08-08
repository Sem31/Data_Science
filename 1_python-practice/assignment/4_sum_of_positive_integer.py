#sum of positive integer

n = int(input("Enter the no. : "))
sum = 0
for i in range(1,n+1):
	sum = sum + i

f = sum*(sum + 1)
formula = f/2
print(formula)
