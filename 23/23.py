

dp = [0]*8
dp[3] = 1
for i in range(4,8):

    if i%2==0:
        dp[i]+=dp[i//2]
    dp[i]+=dp[i-2]
    dp[i]+=dp[i-1]

dp1 = [0] * 23
dp1[7] = dp[7]
for i in range(7, 21):
    if i == 10:
        continue

    if i % 2 == 0:
        dp1[i] += dp1[i // 2]
    dp1[i] += dp1[i - 2]
    dp1[i] += dp1[i - 1]

print(dp1[20])