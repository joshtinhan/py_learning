import sys


class Store:
    all = []

    def __init__(self, item, price, history={}):
        self.item = item
        self.price = price
        self.history = history
        Store.all.append(self)

    def buy(self, name, quantity=0):
        if name in self.history:
            self.history[name] += int(quantity)
        else:
            self.history[name] = int(quantity)


n, m = [v for v in input().split()]
for i in range(int(n)):
    item, price = [v for v in input().split()]
    history = {}
    Store(item, price, history)
for i in range(int(m)):
    name, item, quantity = [v for v in input().split()]
    for j in Store.all:
        if j.item == item:
            j.buy(name, quantity)
while True:
    try:
        exec_func = input().split()
        total = 0
        if exec_func[0] == "A":
            for i in Store.all:
                if exec_func[1] in i.history:
                    total += int(i.history[exec_func[1]]) * int(i.price)
            print(total)
        if exec_func[0] == "B":
            for i in Store.all:
                if i.item == exec_func[2]:
                    if exec_func[1] in i.history:
                        print(i.history[exec_func[1]])
                    else:
                        print("0")
        if exec_func[0] == "C":
            for i in Store.all:
                if i.item == exec_func[1]:
                    if i.history != {}:
                        print(",".join(sorted(i.history.keys())))
                    else:
                        print("0")
    except:
        sys.exit(1)
