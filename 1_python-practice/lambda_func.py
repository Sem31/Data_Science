# Lambda funtion

a = lambda x : x*x 
print("square of 5 is  : ",a(5))

# use for the add two no.

a = lambda x,y  : x+y
print("sum is : ",a(10,20))

#find the square of the 1 to 10 using lambda
# also use of the map function to map(function,sequence)
squ = lambda x : x*x
ans = list(map(squ,range(1,11)))
print(ans)

# find the square b/w 5 to 50 
# use of the filter function to filter(function,sequence) to filterout
check = list(filter(lambda x : (x > 5 and x < 50),ans))
print(check)

