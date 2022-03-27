def is_VPS(s):
    stack = []
    ho = ['[', '(', ')', ']']
    for ps in s:
        if ps in ho:
            if ps == "(" or ps == '[':
                stack.append(ps)
            elif ps == ')':
                if len(stack) != 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif ps == ']':
                if len(stack) != 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
    if stack == []:
        return True
    else:
        return False

while True:
    s = input()
    if s[0] == ".":
        break

    if is_VPS(s):
        print("yes")
    else:
        print("no")