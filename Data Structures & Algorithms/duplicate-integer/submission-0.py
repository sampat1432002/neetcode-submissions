class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = {}
        for i in nums:
            if dups.get(i):
                return True
            else:
                dups[i] = 1
        return False
                