a = list(map(int, input().split()))
a = sorted(set(a), reverse=True)
sl = a[1] if len(a) > 1 else None
print(sl)
