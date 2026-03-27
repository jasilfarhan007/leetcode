class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        a=[]
        for i in nums:
            if nums.count(i)>1:
                a.append(i)
        b=set(a)
        return list(b)
        