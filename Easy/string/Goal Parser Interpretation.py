#Goal Parser Interpretation
class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        print(command)
        out=""
        for i in range(len(command)):
            print(i)
            if command[i]=="G":
                out+="G"
            elif command[i]=="(" and (command[i+1])==")":
                out+="o"
            elif command[i]=="(" and (command[i+1])=="a":
                out+="al"
        print(out)
            
obj=Solution()
#command = "G()(al)"
command = "G()()()()(al)"
obj.interpret(command)
