string = input()
d = {'[' , ']' , '(' , ')' , '{' , '}'}
i = 0
act_int = []
while i < len(string):
    char = string[i]
    en = ''
    if string[i] in d:
        act_int.append(string[i])
    else:
        while i < len(string) and string[i] not in d and string[i] != ',' and string[i] != ' ':
            en += string[i]
            i += 1
        if en:
            act_int.append(float(en))
            i -= 1
    i += 1
stack = []

stack.append('d')
stack.append('d')
res = 0
i = 0
while i < len(act_int):

    char = act_int[i]
    if stack[-1] != '{':
        if char == '(':
            stack.append('(')
            stack.append(0)

        elif char == ')':
            c = stack.pop()
            stack.pop()
            if stack[-2] == '(':
                stack[-1] += c
            elif stack[-2] == '[':
                stack[-1] += (1/c)
            else:
                res = c

        elif char == '[':
            stack.append('[')
            stack.append(0)
            
        elif char == ']':
            c = ( 1 / stack.pop() )
            stack.pop()
            if stack[-2] == '(':
                stack[-1] += c
            elif stack[-2] == '[':
                stack[-1] += (1/c)
            else:
                res = c

        elif char == '{':
            stack.append('{')

        else:
            if stack[-2] == '(':
                stack[-1] += float(char)
            elif stack[-2] == '[':
                stack[-1] += (1/float(char))
    if char == '}':
        stack.pop()

    i += 1
    

print(f"{res:.2f}")

            