s = "{[{]}}"

s = "()[]{}"

valid_stack = []
valid = True

for char in s:
    if char in '[{(':
        valid_stack.append(char)
    elif len(valid_stack) == 0:
        valid = False
        break
    else:
        top_char = valid_stack.pop()
        if char == ')' and top_char == '(':
            continue
        elif char == '}' and top_char == '{':
            continue
        elif char == ']' and top_char == '[':
            continue
        else:
            valid = False
            break
if len(valid_stack):
    valid = False
if valid:
    print('String is valid')