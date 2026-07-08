class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        a=[]
        for i in range(left,right+1):
            n=str(i)
            valid = True
            for j in n:
                if int(j) == 0 or i% int(j) !=0:
                    valid =  False
            if valid:
                a.append(i)
        return a


        