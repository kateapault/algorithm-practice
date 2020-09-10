import os

def alph():
    a = {}
    z = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(0,len(z)):
        a[z[i]] = i+1
    return a

def calculate_name(name):
    tot = 0
    al = alph()
    for x in name:     
        tot += al[x]
    return tot


filepath = os.path.join(os.getcwd(),'project-euler/names.txt')

names = []
with open(filepath) as f:
    for line in f:
        txt = str(line)
        names = txt[1:-1].split('","')

names.sort()

scores = 0
for i in range(0,len(names)):
    scores += calculate_name(names[i]) * (i + 1)

print(scores)