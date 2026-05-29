class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d=list(set(nums))
        if len(nums)!=len(d):
            return True
        else:
            return False