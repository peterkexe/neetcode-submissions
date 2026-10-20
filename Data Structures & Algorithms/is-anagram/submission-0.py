class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = collections.Counter(s)
        freq_t = collections.Counter(t)
        
        if freq_s == freq_t:
            return True
        else:
            return False