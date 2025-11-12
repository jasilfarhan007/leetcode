class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result=[]
        for i in range(len(words)):
            w=words[i]
            if x in w:
                result.append(i)
        return result
        