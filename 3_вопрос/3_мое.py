
f = open('3.1_2.txt')

data = []

for i in f.readlines():
    data.append(list(map(int, i.strip().split())))

m = len(data[0])
n = len(data)

dp_mx = [ [0]*m for i in range(n)]
dp_mn = [ [0]*m for i in range(n)]

dp_mx[0][0]=data[0][0]
dp_mn[0][0]=data[0][0]

mx_fin = 0
mn_fin=999999999
col_fin = 0



for i in range(n):
    for j in range(m):

        var_mx = []
        var_mn = []

        if data[i][j]==-1: continue
        if i==j==0: continue
        if i>0 and i<n and data[i-1][j]!=-1:
            var_mx.append(dp_mx[i-1][j])
            var_mn.append(dp_mn[i-1][j])



        if j>0 and j<m and data[i][j-1]!=-1:
            var_mx.append(dp_mx[i][j-1])
            var_mn.append(dp_mn[i][j-1])

        if var_mn:
            dp_mx[i][j] = max(var_mx) + data[i][j]
            dp_mn[i][j] = min(var_mn) + data[i][j]





        if (i+1>=n or data[i+1][j]==-1) and (j+1>=m or data[i][j+1]==-1):
            col_fin+=1
            mx_fin=max(mx_fin, dp_mx[i][j])
            mn_fin = min(mn_fin, dp_mn[i][j])

print(col_fin, '\n', mx_fin,'\n', mn_fin)
#12 1206 47625