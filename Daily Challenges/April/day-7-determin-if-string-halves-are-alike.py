class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n, half = len(s), len(s) // 2
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        first_half_vowels, second_half_vowels = 0, 0
        for i in range(half):
            if s[i] in vowels:
                first_half_vowels += 1
        for i in range(half, n):
            if s[i] in vowels:
                second_half_vowels += 1

        return first_half_vowels == second_half_vowels
