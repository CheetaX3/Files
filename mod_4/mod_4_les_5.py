class Stack:
    OPEN_BRACKETS = ['(', '[', '{']
    CLOSE_BRACKETS = {')': '(', ']': '[', '}': '{'}
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
    
def is_bracket_sequence_balanced(sequence):
    BRACKET_PAIRS = {'}': '{', ']': '[', ')': '('}
    OPEN_BRACKETS = BRACKET_PAIRS.values()

    stack = Stack()
    for bracket in sequence:
        if bracket in OPEN_BRACKETS:
            stack.push(bracket)
        elif bracket in BRACKET_PAIRS:
            if not stack.is_empty() and stack.peek() == BRACKET_PAIRS[bracket]:
                stack.pop()
            else:
                return False
        else:
            return False
    return stack.is_empty()

sequence = ['[', '(', '{', '(', ')', '}', ')', ']', '[', ']', ']']
print(is_bracket_sequence_balanced(sequence))