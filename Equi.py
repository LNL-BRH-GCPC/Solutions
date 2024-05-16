
inp = input()

specials = "()}{[]"

for special in specials:
    inp = inp.replace(special, " " + special + " ")
    
inp = inp.replace(",", "")

inp = inp.split()

def parallel(values):
    sums = sum([1/val for val in values])
    
    return 1 / sums

def series(values):
    return sum(values)

stack = [[]]

for ch in inp:
    if ch in "[{(":
        stack.append([])
    elif ch.isnumeric():
        stack[-1].append(int(ch))
    elif ch == "]":
        last = stack.pop()
        stack[-1].append(parallel(last))
    elif ch == ")":
        last = stack.pop()
        stack[-1].append(series(last))
    elif ch == "}":
        stack.pop()
        
res = stack[0][0]
print(f"{res:.2f}")