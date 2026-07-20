class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        max_len = 1
        used = set()
        used.add(s[l])
        for r in range(1, len(s)):
            while s[r] in used:
                used.remove(s[l])
                l += 1
            used.add(s[r])
            max_len = max(r-l+1, max_len)
        return max_len