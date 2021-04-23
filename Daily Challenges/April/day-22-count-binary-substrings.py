class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        current_count, previous_count = 0, 0
        current_char = s[0]
        substring_count = 0
        for char in s:
            if char == current_char:
                current_count += 1
            else:
                substring_count += min(current_count, previous_count)
                previous_count = current_count
                current_count, current_char = 1, char

        substring_count += min(current_count, previous_count)
        return substring_count
