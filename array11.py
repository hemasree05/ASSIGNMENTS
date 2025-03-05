a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
c=[]
for i in a1:
    if i in a2 and i not in c:
        c.append(i)
print(c)
