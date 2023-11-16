import shutil
import os
from pathlib import Path
sf=input("Enter source folder path: ")
df=input("Enter destination path: ")
ex=input("Enter extension: ")
if not Path(df).exists():
    os.makedirs(df)
for fo, su, fn in os.walk(sf):
    for i in fn:
        if i.endswith(ex):
            so=os.path.join(fo, i)
            de=os.path.join(df, i)
            shutil.copy(so,de)
