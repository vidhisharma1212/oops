import os

oldname= 'rock.txt'
newname= 'flower.txt'
with open(oldname) as f:
    content=f.read()
with open(newname,"w") as k:
    k.write(content)

os.remove(oldname)