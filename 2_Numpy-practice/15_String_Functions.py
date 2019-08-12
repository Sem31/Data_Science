# String Functions

import numpy as np

#add the two string
print("Add two string : ")
x = np.char.add(['Hello! '],['Welcome to numpy'])
print(x)

#multiply() --> return multiple conatenation
print('\nmultipy two string :')
print(np.char.multiply('Numpy ',3))

#np.char.center(arr,width.fillchar)
print('\nfill all the remaining characters : ')
print(np.char.center('Numpy',10,fillchar = '*'))

#upper() and Capitalize()
print("\ncapitalize the characters and strings : ")
print(np.char.upper('hi'))
print(np.char.upper(['hello','numpy']))

#lower()
print('\nconvert the string and character into the lower : ')
print(np.char.lower('HI'))
print(np.char.lower(['HELLO','SEM']))	

#split()
print('\nSplit the string : ')
print(np.char.split('hello how are you?'))
print(np.char.split('kamlesh,Rtc X Roads,Hyderabad',sep = ','))

#splitlines()
print('\nSplite the line :')
print(np.char.splitlines('Hello\nHow are you?'))

#strip()
print('\nstrip means remove the element from the string : ')
print(np.char.strip('ameerpet','a'))

#join()
print('\nJoins the string and the special characters : ')
print(np.char.join(':','dmy'))
print(np.char.join(['/',':'],['dmy','ymd']))

#replace()
print('\nReplace the string and character : ')
print(np.char.replace("I'm learning Data Science","I'm","We're"))

