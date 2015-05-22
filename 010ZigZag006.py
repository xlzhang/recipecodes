class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if len(s)<numRows or len(s)<=0:
            return s
        # if len(s) == 0:
            # return s
        if numRows ==1:
            return s
        ret = [0]*len(s)
        start = 2*numRows-2
        end = 0
        length = len(s)
        i = 0
        for j in range(numRows):
            #ret.append(s[j])
            ret[i] = s[j]
            i+=1
            while 1:
                print j+start
                print j+end
                if j+start >= length:
                    break
                if start != 0:
                    print j+start
                    ret[i] = s[j+start]
                    i+=1
                    # ret.append(s[j+start])
                    j = j+start
                if end != 0:
                    if j+end >= length:
                        break
                    print j+end
                    ret[i] = s[j+end]
                    i+=1
                    # ret.append(s[j+end])
                    j = j + end
            start = start - 2
            end = end + 2
            j = 0
        return ''.join(ret)

    def convert(self, s, numRows):
        if len(s)<numRows or len(s)<=0 or numRows ==1:
            return s
        length = len(s)
        arr = [[] for x in range(numRows)]
        ret = []
        flag = 0
        i = 0
        j = 0
        while j < length:
            if i < numRows and not flag:
                arr[i] += s[j]
                i += 1
                j += 1
            elif not flag:
                flag = 1
                i -= 1
            else:
                i -= 1
                arr[i] += s[j]
                if i == 0:
                    flag = 0
                    i += 1
                j += 1
        for i in range(len(arr)):
            ret += arr[i]
        return ''.join(ret)
