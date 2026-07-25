class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ht = {}
        for num in nums:
            if ht.get(num,0)==1:
                return True
            ht[num]=ht.get(num,0)+1
        return False


         