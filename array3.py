arr_val=[10, 20, 30, 40, 50]
ele_to_find=30
index=-1
for i, value in enumerate(arr_val):
 if value==ele_to_find:
  index=i
  break
print(index)
