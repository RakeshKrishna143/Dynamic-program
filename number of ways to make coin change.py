'''
Engineer's Revolution
Program to find the number of ways
by which the coins can be added to obtain the sum 
'''

n = 4

coins = [1,2,3]

def count_no_of_ways(coins,n):
    table = [0 for i in range(n+1)]
    table[0] = 1
    
    for coin in coins:
        for i in range(coin,n+1):
            table[i] +=table[i-coin]
            
    return table[n]

print(count_no_of_ways(coins, n))
