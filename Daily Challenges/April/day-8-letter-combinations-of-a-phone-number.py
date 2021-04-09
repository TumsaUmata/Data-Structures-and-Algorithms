class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        n = len(digits)
        phone_number = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv",
                        '9': "wxyz"}

        queue = deque()
        for i in phone_number[str(digits[0])]:
            queue.append(i)

        temp = ""
        for i in range(1, n):
            size = len(queue)
            value = digits[i]
            while size:
                temp = queue.popleft()
                for j in phone_number[value]:
                    queue.append(str(temp + j))
                size -= 1

        return queue
