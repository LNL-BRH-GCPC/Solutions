n = int(input())
arr = list(map(int, input().split()))

nbsection = 0

if arr[0] == 0:
    curr_section = False
else:
    curr_section = True

for i in arr:
    if i == 0 :
        if not curr_section:
            nbsection += 1
            curr_section = True
    else:
        curr_section = False

print(nbsection)