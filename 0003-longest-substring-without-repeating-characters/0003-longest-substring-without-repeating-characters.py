class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        if n ==0 or n==1:
            return n
        maxLength = 0
        l,r=0,0
        mp={}
        while(r<n):
            while(s[r] in mp):
                del mp[s[l]]
                l+=1
            mp[s[r]] = r
            maxLength = max(maxLength, len(mp))
            r+=1
        return maxLength
        