class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        
        if len(s) ==0 or len(s) ==1:
            return True
            
        s = s.lower()
        count=0
        idx1 = 0
        idx2 = len(s)-1
        
        for i in range(len(s)):

            if idx1 >= idx2:
                return True
            if s[idx1].isalnum() == True and s[idx2].isalnum()==True:
                if s[idx1] != s[idx2]:
                    return False
                idx1 +=1
                idx2 -=1
            elif s[idx1].isalnum() == True and s[idx2].isalnum()==False:
                idx2 -=1

            elif s[idx1].isalnum() == False and s[idx2].isalnum()==True:
                idx1 +=1

            elif s[idx1].isalnum() == False and s[idx2].isalnum()==False:
                idx1 +=1
                idx2 -=1
