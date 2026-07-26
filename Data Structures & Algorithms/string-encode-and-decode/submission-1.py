class Solution:

    def encode(self, strs: List[str]) -> str:
        cs = ''

        for s in strs:
            tmp = str(len(s)) + '#' + s
            cs += tmp
        print(cs)
        return cs

    def decode(self, s: str) -> List[str]:
        strs = []
        ptr = 0
        while ptr < len(s):
            idx = s[ptr:].find('#')
            # print(idx)
            length = int(s[ptr:ptr+idx])
            # print(length)
            word = s[ptr+idx+1:ptr+idx+1+length]
            # print(word)
            strs.append(word)
            ptr += idx+1+length
        return strs
            