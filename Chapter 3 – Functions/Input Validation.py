def collatz(number):
    if number%2==0:
        print(number//2)
        return number//2
    else:
        print(3*number+1)
        return 3*number+1
print("Enter number")
while True:
    try:
        x=int(input())
        n=collatz(x)
        if n==1:
            break
    except Exception as e:
        print("Input must be an integer")
        continue