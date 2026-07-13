class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        R, L = 1, 0
        max_l = 1
        while L < len(s) and R < len(s):
            if s[R] not in s[L:R]:
                R += 1
                length = R - L
                if length > max_l:
                    max_l = length
            else:
                L += 1
        return max_l