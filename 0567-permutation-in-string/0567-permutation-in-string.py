class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp={}
        if(len(s1)>len(s2)):
            return False
        for s in s1:
            mp[s] = mp.get(s, 0)+1
        l,r=0,len(s1)-1
        while(r<len(s2)):
            mp1={}
            k=l
            while(k<=r):
                mp1[s2[k]] = mp1.get(s2[k], 0)+1
                k+=1
            if(mp==mp1):
                return True
            l+=1
            r+=1

        return False
