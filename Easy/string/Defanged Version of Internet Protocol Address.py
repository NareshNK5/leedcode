# Python3 implementation to find the
# defanged version of the IP address
# Function to generate a
# defanged version of IP address.
'''
def GeberateDefangIP(str):
    defangIP = "";
    # Loop to iterate over the
    # characters of the string
    for c in str:
        print(c)
        if(c == '.'):
            defangIP += "[.]"
            print(defangIP)
        else:
            defangIP += c;
    return defangIP;
# Driver Code
str = "255.100.50.0";
print(GeberateDefangIP(str));
# This code is contributed by Nidhi_biet
'''

def ip_fun(ip):
    defn=""
    for i in ip:
        if i==".":
            defn+="[.]"
        else:
            defn+=i
    return defn
            
        
ip="127.0.51.0"
print(ip_fun(ip))

'''
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            print(i,j,k)
'''
