a=list(map(int,input().split()))
a_new=[]
for i in a:
    if i not in a_new:
        a_new.append(i)
print(a_new)
