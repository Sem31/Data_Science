first = int(input("Enter the first : "))
second = int(input("Enter the second :"))
third = int(input("Enter the third : "))

m = min(first,second,third)
ma = max(first,second,third)
midel = (first+second+third)-m-ma
print("minimum : ",m)
print("maximum :",ma)
print("remain no : ",midel)
