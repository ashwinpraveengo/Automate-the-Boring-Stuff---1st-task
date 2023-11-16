def printTable(L):
	colWidths=[]
	for i in range(len(L)):
		for j in L[i]:
			colWidths.append(len(j))
	m=max(colWidths)
	for i in range(len(L[i])):
		for j in L:
			print(j[i].rjust(m),end='')
		print()
L=[['apples', 'oranges', 'cherries', 'banana'],['Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'goose']]
printTable(L)