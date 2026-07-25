class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest_string = ''
        current_min_length = float('inf')
        for string in strs:
            if len(string) < current_min_length:
                smallest_string = string
                current_min_length = len(string)
        
        # print(f'Smallest string : {smallest_string}')
        for i in range(0, current_min_length + 1):
            prefix = smallest_string[:i]
            # print(prefix)
            for s in strs:
                if prefix != s[:i]:
                    return prefix[:i-1]
        return prefix