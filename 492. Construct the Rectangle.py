class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        a= int(sqrt(area))
        while area % a:
            a -= 1
        return [area//a,a]
        