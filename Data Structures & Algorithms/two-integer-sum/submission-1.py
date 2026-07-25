class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            idx = hashmap.get(target - n)
            if idx is not None:
                return [idx, i]
            hashmap[n] = i

            