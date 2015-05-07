class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        count = 0
        for i in range(2,n+1):
            if i ==2:
                count +=1
            else:
                isprime =0
                for j in range(2,i+1):
                    if i%j !=0:
                        isprime +=1
                if isprime==1:
                    count +=1
        return count
