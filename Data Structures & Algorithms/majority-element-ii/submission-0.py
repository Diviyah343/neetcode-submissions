class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        s=set(nums)
        n=len(nums)
        res=[]
        for i in s:
            if nums.count(i)> n/3:
                res.append(i)

        return res