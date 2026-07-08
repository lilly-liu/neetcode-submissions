class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}
        for c in s:
            ds[c] = ds.get(c, 0) + 1
        for ch in t:
            dt[ch] = dt.get(ch, 0) + 1
        return ds == dt
                
        