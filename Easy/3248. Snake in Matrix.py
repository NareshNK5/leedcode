class Solution:
    def finalPositionOfSnake(self, n: int, commands: list[str]) -> int:
        row,col = 0,0
        for command in commands:
            if command == "RIGHT":
                col+=1
            elif command == "LEFT":
                col-=1
            elif command == "DOWN":
                row+=1
            elif command == "UP":
                row-=1
        return row*n+col
n=3
commands = ["DOWN","RIGHT","UP"]
obj = Solution()
res = obj.finalPositionOfSnake(n,commands)
print(res)