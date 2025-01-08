'''
def is_palindrome(s):
    s = s.lower()
    start = 0
    end = len(s) - 1
    while start < end:
        if not s[start].isalnum():
            start += 1
            continue
        if not s[end].isalnum():
            end -= 1
            continue
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True
string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
'''

#------------------------type 2----------------------
'''
def is_palindrome(s):
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned_s == cleaned_s[::-1]
string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
'''


#-----------------------------type 3-----------------------
# def is_palindrome(s):
#     cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
#     length = len(cleaned_s)
#     for i in range(length // 2):
#         if cleaned_s[i] != cleaned_s[length - i - 1]:
#             return False
#     return True
# string = input("Enter a string: ")
# if is_palindrome(string):
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

#------------------------------type 4-------------------

def ispoli(string):
    left=0
    right=len(string)-1
    if (left<right):
        while (string[left]!=string[right]):
            return False
        left+=1
        right-=1
    return True

string = "madam"
if ispoli(string):
    print(string + " is palindrome") 
else:
    print(string + " is not a palindrome" )