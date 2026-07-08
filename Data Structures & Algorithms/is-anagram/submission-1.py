class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}
        for c in s:
            if c not in ds:
                ds[c] = 1
            else:
                ds[c] += 1
        for ch in t:
            if ch not in dt:
                dt[ch] = 1
            else:
                dt[ch] += 1
        return ds == dt
                
        