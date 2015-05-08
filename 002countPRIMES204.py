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


import math
class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n<3:
            return 0
        else:
            arr = [True]*n
            i=2
            #while i < math.sqrt(n):
            for i in range(2,int(math.sqrt(n))+1):
                if arr[i]:
                    #for j in range(i,n):
                    j =i
                    while j*i<n:
                        arr[i*j]=False
                        j +=1
                #i+=1
            return sum(arr)-2
