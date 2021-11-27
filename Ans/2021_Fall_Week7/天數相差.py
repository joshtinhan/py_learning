from datetime import date
date_arr = []
for i in range(2):
    [y, m, d] = [int(v) for v in input().split()]
    date_arr.append(date(y, m, d))
print(abs((date_arr[1]-date_arr[0]).days))
