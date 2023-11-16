def comma(L):
	if len(L)==0:
		print("Nothing to be printed")
	else:
		for i in range(len(L)-1):
			print(f'{L[i]}, ',end='')
		print(f'and {L[len(L)-1]}',end='')
a=eval(input("Enter list of elements as ['apples','banana']"))
comma(a)