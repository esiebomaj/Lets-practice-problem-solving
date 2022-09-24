class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for i in nums:
            if i in freq:
                return True
            freq[i] = True
        return False
            