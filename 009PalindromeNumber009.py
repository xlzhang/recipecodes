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
    
    def isPalindrome(self, x):

        if x<0:
            return False
        ret = 0
        temp_x = x
        while temp_x!=0:
            ret = ret*10 + temp_x%10
            temp_x = temp_x/10
        if ret>2**31-1 or ret< -2**31 or x!=ret:
            return False
        return True

class Solution {
public:
 
    bool check(int x, int &y){
        if (x==0) {return true;}
        if (check(x/10,y)){
            if (x%10==y%10){
                y=y/10;
                return true;
            }
        }
        return false;
    }
    bool isPalindrome(int x) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        if (x<0){return false;}
        return check(x,x);
    }
};
