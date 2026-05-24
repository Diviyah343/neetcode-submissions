class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0
        longest = 0

        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            max_freq = max(counts.values())
            while (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest