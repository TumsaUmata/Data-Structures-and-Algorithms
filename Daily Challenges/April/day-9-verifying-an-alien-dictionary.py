class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabets = {value: key for key, value in enumerate(order)}
        previous = []
        for i in range(len(words)):
            word = [alphabets[char] for char in words[i]]
            if word < previous:
                return False
            previous = word
        return True
