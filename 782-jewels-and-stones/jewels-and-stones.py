class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        count = 0
        for x in stones:
            if x in s:
                count += 1
        return count