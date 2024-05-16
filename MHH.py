

n = int(input())
horses = []

for _ in range(n):
    horses.append(int(input()))
    
budget = int(input())
horsesBuy = int(input())

combs = []
cur = []
curSum = 0

horses = list(set(horses))

def bac(idx):
    global curSum
    if idx == len(horses) or len(cur) == horsesBuy:
        if curSum == budget and len(cur) == horsesBuy:
            combs.append(sorted(cur))
        return
    
    cur.append(horses[idx])
    curSum += horses[idx]
    bac(idx + 1)
    cur.pop()
    curSum -= horses[idx]
    bac(idx + 1)
    
bac(0)

print(combs)