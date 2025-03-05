a=list(map(int,input().split()))
mn=a[0]
mx=a[0]
for i in a:
    if i<mn:
        mn=i
    if i>mx:
        mx=i
print(mx-mn)
