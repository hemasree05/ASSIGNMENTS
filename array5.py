def remove_ele(arr, value):
 arr.remove(value)
 return arr
array_val=[10, 20, 30, 40, 50]
val_to_remove=30
result=remove_ele(array_val, val_to_remove)
print(result)
