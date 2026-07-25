class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for n in nums:
            if hashmap.get(n):
                return True # we have a duplicate
            hashmap[n] = True # if not; insert the element in the hashmap
        return False # if loop breaks, all numbers are traversed; no duplicates found