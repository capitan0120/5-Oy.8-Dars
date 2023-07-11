class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()):
            return False
        HashMap = {}
        for i, j in zip(pattern, s.split()):
            if i not in HashMap:
                HashMap[i] = j
            else:
                if HashMap[i] != j:
                    return False
        return False if len(set(HashMap.values())) != len(HashMap) else True
