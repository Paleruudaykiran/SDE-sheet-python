def findMaxConsecutiveOnes(nums):
        ct,maxi = 0,0
        for x in nums :
            if x == 0 :
                ct = 0
            else :
                ct += 1
                maxi = max(maxi,ct) 
        return maxi