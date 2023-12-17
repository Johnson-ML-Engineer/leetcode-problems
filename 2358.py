"""You are given a positive integer array grades which represents the grades of 
students in a university. You would like to enter all these students into a
 competition in ordered non-empty groups, such that the ordering meets the 
 following conditions:

The sum of the grades of students in the ith group is less than the sum of the 
grades of students in the (i + 1)th group, for all groups (except the last).
The total number of students in the ith group is less than the total number of 
students in the (i + 1)th group, for all groups (except the last).
Return the maximum number of groups that can be formed.

 """
class Solution:
    def maximumGroups(self, grades):
        total = 0
        for i in range(1,len(grades)+1):
            total += i
            if total == len(grades):
                return i
            if total > len(grades):
                return i-1
           
        