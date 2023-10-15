nums = [1,3,5,4,7]
l=1
c=1

def findNumberOfLIS( nums: list[int]) -> int:
        if not nums:
            return 0
        val=1
        cnt=1
        dp1=[1]*len(nums)
        dp2= [1]*len(nums) 
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    if dp1[j]+1>dp1[i]:
                        dp1[i],dp2[i]=dp1[j]+1,dp2[j] 
                    elif dp1[j]+1==dp1[i]:
                        dp2[i]+=dp2[j]    
            if dp1[i]>val:
                val,cnt=dp1[i],dp2[i]
            elif dp1[i]==val:
                cnt+=dp2[i]
        return cnt
        

        
   
    
    