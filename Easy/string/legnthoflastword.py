# Python3 program for implementation of efficient
# approach to find length of last word
def length(strn):
# Split by space and converting
# String to list and
	lis = list(strn.split(" "))
	return len(lis[-1])


# Driver code
strn = "Geeks for Geeks"
print("The length of last word is",
	length(strn))

# This code is contributed by vikkycirus

'''# Python3 program for implementation of simple
# approach to find length of last word
def lengthOfLastWord(a):
        print(a)
        l = 0
        # String a is 'final'-- can not be modified
        # So, create a copy and trim the spaces from
        # both sides
        x = a.strip()
        print(x)
        for i in range(len(x)):
            if x[i] == " ":
                l = 0
                print("test1",x[i])
            else:
                l += 1
                print("test2",x[i])
                print(l)
        return l
# Driver code
if __name__ == "__main__":
	inp = "  Geeks For Geeks "
	print("The length of last word is",
		lengthOfLastWord(inp))
# This code is contributed by
# sanjeev2552
'''
