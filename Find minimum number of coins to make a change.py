coins=[1,2,5]
n = 11

table = [0]+[float('inf')]*n

for coin in coins:
    for i in range(coin,n+1):
        table[i]=min(table[i],table[i-coin]+1)
        
print(table[n])
