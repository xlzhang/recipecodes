class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x >=0 and x <10:
            return True
        elif x <0:
            return False
        arr = []
        while x!=0:
            lastdigit = x%10
            arr.append(lastdigit)
            x = x/10
        i = 0
        length = len(arr)
        while i <= (length-1)/2 :
            if arr[i] != arr[length-i-1]:
                return False
            i += 1
        return True
