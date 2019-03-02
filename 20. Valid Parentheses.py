class Solution:
    def isValid(self, s: 'str') -> 'bool':
        mapping = {")": "(", "}": "{", "]": "["}
        ss = []

        for i in range(len(s)):
            if s[i] not in mapping:
                ss.append(s[i])
            else:
                if len(ss) == 0:
                    return False
                elif mapping[s[i]] != ss[-1]:
                    return False
                else:
                    ss.pop()

        if len(ss) == 0:
            return True
        else:
            return False

