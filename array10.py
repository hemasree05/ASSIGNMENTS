a=list(map(int,input().split()))
d=[]
u=[]
for i in a:
    if i in u:
        d.append(i)
    else:
        u.append(i)
print(d)
