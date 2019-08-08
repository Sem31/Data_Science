n = input("Enter the no : ")
print(n)
print(n[::-1])
if (n == n[::-1]):
	print("{} is palindrome!".format(n))
else:
	print("{} is not palindrome!".format(n))

