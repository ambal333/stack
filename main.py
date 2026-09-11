from Stack import Stack

stack1 = Stack()

def checking_balance(stack: Stack,staples: str) -> str:
    staples_dict = {')': '(', ']': '[', '}': '{'}
    for i in staples:
        if i in '([{':
            stack.push(i)
        elif i in ')}]':
            if stack.is_empty():
                return 'Несбалансированно'
            if stack.peek() == staples_dict.get(i):
                stack.pop()
            else:
                return 'Несбалансированно'
    if stack.is_empty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'

print(checking_balance(stack1,'{}'))
