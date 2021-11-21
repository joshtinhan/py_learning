
arr = [1, 2, 3, 4, 5]
b = arr.pop(3)
arr = arr[0:3]+[b]+arr[2+1::]
print(arr)
