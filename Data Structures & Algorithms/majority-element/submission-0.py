import statistics

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        re= statistics.mode(nums)
        return re