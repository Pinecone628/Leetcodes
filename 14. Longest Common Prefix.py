class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        p = ""
        strs.sort()
        for i, j in zip(strs[0], strs[-1]):
            if i == j:
                p += i
            else:
                break
        return p
