import re
import os 
from pathlib import Path
foldpath=input("Enter folder path : ")
if not Path(foldpath).exists():
    print("No folder found !")


else:
    y=input("Enter expression to be searched : ")
    c=0
    for fo,so,fn in os.walk(foldpath):
        for i in fn:
            if i.endswith('txt'):
                f=open(i,"r")
                x=f.readlines()
                for j in x:
                    for k in j.split():
                        if re.search(y,k,re.IGNORECASE):
                            print(f"The file name is {i} and line is {j}")
                            c=1
    if c==0:
        print("No expression found")
        
                
