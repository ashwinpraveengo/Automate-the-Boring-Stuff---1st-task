import random
L=[]
x=['H','T']
numberofstreaks=0
for j in range(100):
    t=random.choice(x)
    L.append(t)
c=0
for i in range(0,len(L)):
    if i+5<=len(L):
        if L[i]==L[i+1]==L[i+2]==L[i+3]==L[i+4]==L[i+5]:
            c+=1
print('Chance of streak: %s%%' % (c / 100))