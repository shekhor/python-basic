def is_balanced(expression):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    for char in expression:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if not stack or stack.pop() != brackets[char]:
                return False
    return not stack

parentheses = "({[()]})"
print(is_balanced(parentheses))
