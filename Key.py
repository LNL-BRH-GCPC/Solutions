string = input().split()

buffer = ''
buffc = ''
i = 0
stack = []
while i < len(string):
    if string[i] == 'Ctrl' and string[i+2] == 'V':
        i += 2
        buffer += buffc
    elif string[i] == 'Ctrl' and string[i+2] == 'C':
        i += 2
        buffc = buffer
    elif string[i] == 'Ctrl' and string[i+2] == 'X':
        i += 2
        buffc = buffer
        buffer = ''
    else:
        buffer += string[i] + ' '
    i += 1 

print(buffer)