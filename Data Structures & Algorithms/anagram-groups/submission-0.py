class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for str in strs:
            sorted_string = "".join(sorted(str))
            if sorted_string not in res:
                res[sorted_string] = [str]
            else:
                res[sorted_string].append(str)        
        return list(res.values())
