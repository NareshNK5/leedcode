class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seat=set(seats)
        cc=0
        stud=sorted(students)
        for i in range(len(seat)):
            seats=(list(seat))
            c=seats[i]-stud[i]
            cc+=c
        print(abs(cc))
seats = [2,2,6,6]
students = [1,3,2,6]
obj = Solution()
obj.minMovesToSeat(seats,students)