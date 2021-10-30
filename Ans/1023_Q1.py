from decimal import *
# v, a, s, t = list(
#     map(Decimal, input('Please enter the params').split(',')))

# print(s)
inputArr = input('Please enter the params').split(',')
for index, value in enumerate(inputArr):
    if value != '':
        inputArr[index] = float(inputArr[index])
[input_v, input_a, input_s, input_t] = inputArr


def calc(v, a, s, t):
    v_0 = float(1.0)
    if v == '':
        v = v_0 + a * t
    if a == '':
        if s == '':
            a = (v**2 - v_0**2)/s*2
        a = (v-v_0)/t
    if s == '':
        s = v_0 * t + (a * t**2)/2
    if t == '':
        t = (v-v_0)/a
    print(f"v={v}, v0=1.0, a={a}, S={s}, t={t}")


calc(input_v, input_a, input_s, input_t)
