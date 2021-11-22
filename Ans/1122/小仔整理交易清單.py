class store:
    def __init__(self, item, price, customs=[]):
        self.item = item
        self.price = price
        self.customs = customs
    def buy(self,custom):
        self.customs.append(custom)
n, m = [v for v in input().split()]
allInfo = []
for i in range(int(n)):
    item, price = [v for v in input().split()]
    allInfo.append(store(item,price))
# item1 = store("apple",120)
# item1.buy("Jeff")
print(allInfo[0].item)