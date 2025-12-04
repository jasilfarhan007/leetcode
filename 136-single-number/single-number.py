class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ab=[x for x in nums if nums.count(x)==1]
        return ab[0]
       