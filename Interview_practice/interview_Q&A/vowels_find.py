def get_vowels(String):
    return [each for each in String if each in "aeiou"]
get_string1 = "hello"
print("The Vowels Are:  ",get_vowels(get_string1))