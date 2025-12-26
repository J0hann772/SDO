

def f(x, st, end):
    a = st<=x<=end
    t = 280<=x<=480
    s = 223<=x<=480
    return (a) or (t==s)


x_arr = [x for x in range(100,500)]
res = []

for x in x_arr:
    if not f(x, 0, 0):
        res.append(x)

fl = True

for i in range(0, 500):
    if not f(i, min(res), max(res)):
        fl = False
        print(f)

print(max(res)- min(res)+1, min(res), max(res))


