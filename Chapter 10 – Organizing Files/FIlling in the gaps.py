import os
import re

def fg(folder, p):
    fs = os.listdir(folder)
    pat = re.compile(rf'^({p})(\d+)(\.txt)$')
    nf = [(f, int(m.group(2))) for f in fs if (m := pat.match(f))]
    if not nf:
        return
    nf.sort(key=lambda x: x[1])
    en = nf[0][1]
    for f, n in nf:
        if n != en:
            old = os.path.join(folder, f)
            new = os.path.join(folder, f'{p}{en:03}.txt')
            os.rename(old, new)
        en += 1
fg('folder_path', 'spam')
