class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
       a=[i for i in order if i in friends]
       return a
