import random
import time

for i in range(10):
    x=random.randint(0,9)
    y=random.randint(0,9)
    product=x*y
    trs=3
    st=time.time()

    while time.time()-st < 8 and trs > 0:
        z=input(f"Enter the product of {x} and {y}: ")
        try:
            z=int(z)
            if z==product:
                print("CORRECT!")
                time.sleep(1)
                break
            else:
                print("Incorrect! Please Try again.")
                trs-=1
        except ValueError:
            print("Invalid input! Please enter a integer ")

    if trs == 0 or time.time()-st >= 8:
        print(f"Time's up! The correct answer is {product}.\n")
