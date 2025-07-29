OPEN_BRACKETS = ['(', '[', '{']
CLOSE_BRACKETS = {')': '(', ']': '[', '}': '{'}

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Стек пуст")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Стек пуст")


my_stack = Stack()
balanced = True
parenthesis_sequence = ['[', '(', '{', '(', ')', '}', ')', ']', '[', ']']

for i in parenthesis_sequence:
    if i in OPEN_BRACKETS:
        my_stack.push(i)
    elif i in CLOSE_BRACKETS:
        if not my_stack.is_empty() and my_stack.peek() == CLOSE_BRACKETS[i]:
            my_stack.pop()
        else:
            balanced = False
            break

if balanced and my_stack.is_empty():
    print("Сбалансированная скобочная последовательность")
else:
    print("Несбалансированная скобочная последовательность")