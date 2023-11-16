f=open("anv.txt","r")
x=f.read().split()
print(x)
for i in range(len(x)):
	if x[i].startswith("ADJECTIVE"):
		print("Enter an adjective:")
		a=input()
		x[i]=a
	elif x[i].startswith("NOUN"):
		print("Enter a noun:")
		n=input()
		x[i]=n
	elif x[i].startswith("ADVERB"):
		print("Enter a verb:")
		v=input()
		x[i]=v
	elif x[i].startswith("VERB"):
		print("Enter a verb:")
		v=input()
		x[i]=v
f=open("anv.txt","w")
for i in x:
	f.write(f"{i} ")
f.close()

