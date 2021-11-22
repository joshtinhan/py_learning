def perm(a, k=0):
    global maxv, maxe
    weight = 0
    val = 0
    if k == len(a):
        # print(a, end="")
        for m in range(len(a)):
            pv = a[m]
            mw = int(w[pv-1])
            mv = int(v[pv-1])

            weight = weight+mw
            if weight > 10:
                break
            val = val+int(v[pv-1])
            if val > maxv:
                maxv = val
                maxe = a[0:m+1]
            print(' ', weight, val, maxv)
        weight = 0
        val = 0
    else:
        for i in range(k, len(a)):
            a[k], a[i] = a[i], a[k]
            perm(a, k+1)
            a[k], a[i] = a[i], a[k]


maxe = []
maxv = 0
n = 5
c = 10
w = [2, 2, 6, 5, 4]
v = [6, 3, 5, 4, 6]
perm([1, 2, 3, 4, 5])
