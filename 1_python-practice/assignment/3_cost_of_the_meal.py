meal = int(input("Enter the amount of the meal : "))

gst = meal * 18/100
tax = meal + gst
print("Your meal price is : ",meal)
print("your meal price with 18% gst : ",tax)

tip = meal * 18/100
total = tax + tip
print("18% of the waiter tips without tax {}  then your total meal price is : {}".format(tip,total))
