#remove vowels

strn="What"
vowels=["a","e","i","o","u"]

def rm_vowels(strn):
    strn1=""
    for strn in strn.lower():
        if strn not in vowels:
            strn1+=strn
    return strn1
out=rm_vowels(strn)
print(out)
