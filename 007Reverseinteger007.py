class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        ret = 0
        flag = 0
        if x<0:
            flag=1
            x = -x
        
        lastdigit = 0
        while lastdigit ==0 and x<10:
            if ret >2**31:
                return 0
            else:
                lastdigit = x%10
                # if lastdigit ==0 and x<10:
                    # break
                ret = ret*10+lastdigit
                x = x/10
        if flag==1:
            return -ret
        return ret
