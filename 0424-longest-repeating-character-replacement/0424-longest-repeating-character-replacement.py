class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_count={}
        l,r,max_freq,max_len=0,0,0,0
        while(r<len(s)):
            freq_count[s[r]] = freq_count.get(s[r],0)+1
            max_freq = max(max_freq,freq_count[s[r]])
            if(r-l+1-max_freq > k):
                freq_count[s[l]]-= 1
                l+=1
            max_len = max(max_len, r-l+1)
            r+=1
        
        return max_len

            
                

