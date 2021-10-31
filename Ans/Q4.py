# input1
# 99 2050 免運
# 0
# 5 1999 2.05% 免運
# 5 2000 運費120
# input2
# 81530 99 免運 滿90打99折
# 6 599 2.5% 運費100 滿590打8折,滿300打79折,滿400打9折
# 6 100 運費100 滿590打8折
# 6 600 5% 運費10 滿300打6折,滿400打75折,滿590000000打1折

import math
the_lowest_price = math.inf
for i in range(4):
    inputArr = input("Please input the details:").split()
    if inputArr != ["0"]:
        [quantity, price] = inputArr[:2]
        price = int(price)
        quantity = int(quantity)
        bonus = 1
        discountedPrice = float(price)
        shipping_fee = int()
        for v in inputArr:
            if v[:2] == "運費":
                shipping_fee = int(v[2:])
            elif v == "免運":
                shipping_fee = 0
            elif v[0] == "滿":
                discountArr = v.split(",")
                for discountArrContent in discountArr:
                    [spent, discountRate] = discountArrContent[1:-1].split("打")
                    spent = int(spent)
                    if int(discountRate)/10 > 1:
                        discountRate = float(discountRate)*0.01
                    else:
                        discountRate = float(discountRate)*0.1
                    if price > spent:
                        discountedPrice = min(
                            discountedPrice, price * discountRate)
            elif v[-1] == "%":
                bonus = 1-float(v[:-1])/100
            the_lowest_price = min(
                round((discountedPrice + shipping_fee)*bonus), the_lowest_price)
print(the_lowest_price)
