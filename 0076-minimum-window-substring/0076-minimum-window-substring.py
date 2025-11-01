class Solution:
    def minWindow(self, s: str, t: str) -> str: 
        if len(s) < len(t):
            return ""
        cnt,sIndex,minLength=0,-1,float('inf')
        freq={}
        l,r=0,0
        m,n = len(t),len(s)
        for j in range(0, len(t)):
            freq[t[j]] = freq.get(t[j],0)+1
        while(r<len(s)):
            if(s[r] in freq and freq[s[r]]>0):
                cnt+=1
            freq[s[r]] = freq.get(s[r],0)-1
            while cnt==len(t):
                if(r-l+1<minLength):
                    minLength = r-l+1
                    sIndex = l
                freq[s[l]]+=1
                if(freq[s[l]]>0):
                    cnt-=1
                l+=1
            r+=1
                    


        if sIndex == -1:
            return ""
        else:
            return s[sIndex : sIndex + minLength]


                
                

        