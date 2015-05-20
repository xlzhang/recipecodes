class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        if str =='':
            return 0
        length = len(str)
        i = 0
        space_num = 0
        ret = 0
        flag = 0
        digit_flag = 0
        while i<length:
            if str[i] == ' ':
                space_num += 1
                space_flag = 1
                if space_num == length-1 or flag == 1 or flag == 2:
                    return 0
                elif digit_flag == 1:
                    return ret
                i += 1
            elif str[i] == '-':
                if flag == 1 or flag == 2:
                    return 0
                flag = 1
                i += 1
            elif str[i] == '+':
                if flag == 1 or flag == 2:
                    return 0
                flag = 2
                i += 1
            elif str[i].isalpha():
                break
            else:
                digit_flag = 1
                ret = ret*10 + int(str[i])
                if ret >= 2**31 and (flag == 2 or flag == 0):
                    return 2**31-1
                elif ret >= 2**31 and (flag == 1):
                    return -2**31
                i += 1
        if flag == 1:
            return -ret
        return ret
        
        
    def myAtoi(self, str):
        if str=="":
            return 0
        i=0
        flag = 1
        ret = 0
        while str[i]==' ':
            i += 1
        if str[i] == '+':
            flag = 1
            i += 1
        elif str[i]=='-':
            flag = 0
            i += 1
        if not str[i].isdigit():
            return 0
        while str[i].isdigit():
            if flag == 1 and (ret > 2**31/10):
                return 2**31-1
            elif flag == 1 and (ret == 2**31/10) and int(str[i])>=7:
                return 2**31-1
            elif flag == 0 and (ret > 2**31/10):
                return -2**31
            elif flag == 0 and (ret == 2**31/10) and int(str[i])>=8:
                return -2**31
            else:
                ret = ret*10 + int(str[i])%10
                i += 1
                if i>= len(str):
                    break
        if flag == 0:
            return -ret
        return ret
