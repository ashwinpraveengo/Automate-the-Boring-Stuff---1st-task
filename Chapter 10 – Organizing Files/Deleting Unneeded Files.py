import os
sf=input("Enter source folder path: ")
for fo,su,fn in os.walk(sf):
    for i in fn:
        fp=os.path.join(fo, i)
        fs=os.path.getsize(fp)
        if fs > 100 * 1024 * 1024:  
            print(f"{fp}: {fs} bytes")
