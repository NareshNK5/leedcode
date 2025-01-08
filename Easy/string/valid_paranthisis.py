# # Python3 program to check for
# # balanced brackets.
# # function to check if
# # brackets are balanced
# def areBracketsBalanced(expr):
#     stack = []
#     # Traversing the Expression
#     for char in expr:
#         if char in ["(", "{", "["]:
#             # Push the element in the stack
#             stack.append(char)
#             print(stack)
#         else:
#             # IF current character is not opening
#             # bracket, then it must be closing.
#             # So stack cannot be empty at this point.
#             if not stack:
#                     return False
#             current_char = stack.pop()
#             if current_char == '(':
#                     if char != ")":
#                         return False
# 	        if current_char == '{':
#                     if char != "}":
#                         return False
#             if current_char == '[':
#                     if char != "]":
#                         return False
#         # Check Empty Stack
#         if stack:
#             return False
#         return True
# # Driver Code
# if __name__ == "__main__":
#     expr = "{()}[]"
#     # Function call
#     if areBracketsBalanced(expr):
#         print("Balanced")
#     else:
#         print("Not Balanced")
# # This code is contributed by AnkitRai01 and improved
# # by Raju Pitta



def is_valid_parentheses(s: str) -> bool:
    stack = []
    matching_parentheses = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in matching_parentheses.values():
            stack.append(char)
        elif char in matching_parentheses.keys():
            if stack == [] or matching_parentheses[char] != stack.pop():
                return False
    return stack == []

# Examples
print(is_valid_parentheses("()"))          # True
print(is_valid_parentheses("()[]{}"))      # True
print(is_valid_parentheses("(]"))          # False
print(is_valid_parentheses("([)]"))        # False
print(is_valid_parentheses("{[]}"))        # True
