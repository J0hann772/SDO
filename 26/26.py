
f = open('26_input.txt')
data = f.readlines()[1:]

for i in range(len(data)):
    data[i]=list(map(int, data[i].strip().split()))

"""arr = [[0, -2]]*1_000_001     кол подряд   последний посещенный       """
arr = []
for i in range(1_000_001):
    arr.append([0, -2])

data.sort(key=lambda x: x[0])
print(data[:3])
mx_col = 0
mx_n = 0
for n, t in data:
    f = True
    if n==arr[t][1]:
        continue


    if n == arr[t][1]+1:
        arr[t][0]+=1
    else:
        arr[t][0]=1


    arr[t][1] = n

    if mx_col<arr[t][0]:
        mx_col=arr[t][0]
        mx_n=t
    if mx_col == arr[t][0]:
        mx_n=min(mx_n, t)



print(mx_col, mx_n)


