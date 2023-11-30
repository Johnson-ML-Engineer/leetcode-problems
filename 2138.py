"""A string s can be partitioned into groups of size k using the following procedure:

The first group consists of the first k characters of the string, the second group
 consists of the next k characters of the string, and so on. Each character can be
   a part of exactly one group.
For the last group, if the string does not have k characters remaining, a character
 fill is used to complete the group.
Note that the partition is done so that after removing the fill character from the
 last group (if it exists) and concatenating all the groups in order, the resultant
   string should be s.

Given the string s, the size of each group k and the character fill, return a string
 array denoting the composition of every group s has been divided into, using the
   above procedure.

question no 2138   
 """

class Solution:
    def divideString(self, s, k, fill):
        output = []
        if k > len(s):
            last = s+""
            for i in range(k-len(s)):
                last += fill
            output.append(last)
            return output

        if len(s)%k == 0:
            for i in range(len(s)):
                output.append(s[i*k:i*k+k])
                if i == len(s)//k-1:
                    break
        else:
            for i in range(len(s)):
                output.append(s[i*k:i*k+k])
                if i == len(s)//k-1:
                    n = len(s)%k
                   
                    last = "" + (s[len(s)-n:])
                    for j in range(k-n):
                        last += fill
                    output.append(last)
                    break
        return output
   

        