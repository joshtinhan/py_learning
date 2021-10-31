##input1:,0.16,75,25
##output1:v=5.0, v0=1.0, a=0.16, S=75.0, t=25.0
##input2:0,,2,4
##output2:v=0.0, v0=1.0, a=-0.25, S=2.0, t=4.0


list = [str(n) for n in input().split(",")]
v0 = float(1)
v = list[0]
a = list[1]
S = list[2]
t = list[3]

if v =="" and a != "" and t != "":
    v = v0 + float(a)*float(t)
      
elif S == "" and a != "" and t != "":
    S = v0*float(t) + 0.5*float(a)*float(t)*float(t)
      
elif a == "":
    if v != "" and t != "" and float(t) != 0:
        a = (float(v)-v0)/float(t)
    elif t != "" and S != "" and float(S) != 0:
        a = (float(t)*float(t) - v0*v0)/(2*float(S))

elif t =="":
    if v != "" and a != "" and float(a) != 0:
        t = (float(v)-v0)/float(a)
    elif S != "" and v != "" and (float(v)+v0) != 0:
        t = (2*float(S))/(float(v)+v0)

print(f'v={float(v)}, v0={float(v0)}, a={float(a)}, S={float(S)}, t={float(t)}')
