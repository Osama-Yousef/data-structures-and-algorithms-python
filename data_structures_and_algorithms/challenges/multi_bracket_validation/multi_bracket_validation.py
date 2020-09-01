from queue import LifoQueue


def multi_bracket_validation(value: str) -> bool:
    if len(value) % 2 != 0:
        return False

    closing_values = {'(': ')', '{': '}', '[': ']'}
    open_chars = closing_values.keys()
    stack = LifoQueue(len(value))

    for char in value:
        if char in open_chars:
            stack.put(char)
        else:
            if stack.empty():
                return False
            if closing_values[stack.get()] != char:
                return False

    return stack.empty() 
    