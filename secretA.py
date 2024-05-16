n = input()

adjacency = { 
    "0": ["8" , "0"],
    "1": ["2", "4", "1"],
    "2": ["1", "3" , "5", "2"],
    "3": ["2", "6", "3"],
    "4": ["1", "5", "7", "4"],
    "5": ["2", "4", "6", "8", "5"],
    "6": ["3", "5", "9", "6"],
    "7": ["4", "8", "7"],
    "8": ["0", "5", "7", "9", "8"],
    "9": ["6", "8", "9"]
}

combinations = []
current = []

def generate_combs (idx) :
    if idx == len(n) :
        combinations. append ( "".join(current) )
        return
    for adj in adjacency[n[idx]]:
        current .append(adj)
        generate_combs (idx+1)
        current. pop()

generate_combs(0)
print(*sorted (combinations) )