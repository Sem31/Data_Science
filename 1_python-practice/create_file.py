#create file and write 

with open('k.txt','w') as f :
	f.write('kamlesh')

#add data in file
with open('k.txt','a+') as f:
	f.write(' sem prajapat')

#read file
with open('k.txt','r') as f:
	print(f.read())
