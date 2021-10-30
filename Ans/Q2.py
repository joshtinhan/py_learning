inputArr = input("Please enter the params:").split()
for index in range(len(inputArr)):
    if int(float(inputArr[index])) > 255:
        inputArr[index] = 255
    if int(float(inputArr[index])) < 0:
        inputArr[index] = 0
    inputArr[index] = format(int(float(inputArr[index])), "x")
    if len(list(inputArr[index])) == 1:
        inputArr[index] = '0'+inputArr[index]
[r, g, b] = inputArr
print(f'0x{r}{g}{b}')
