class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        helper = {}
        result = []
        for s in strs:
            key = ''.join(sorted(s))
            if key in helper:
                helper[key].append(s)
            else:
                helper[key] = [s]

        for value in helper.values():
            result.append(value)
        return result
         