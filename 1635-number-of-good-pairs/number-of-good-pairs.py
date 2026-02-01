class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=Counter()
        pair=0
        for x in nums:
            pair+=count[x]
            count[x]+=1
        return pair
        