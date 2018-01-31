# https://www.hackerrank.com/contests/cs5800-f17-init/challenges/second-maximum-element-in-a-list/problem
# Given a list of integers as input, find and output the second maximum element in it. Assume that all the elements are unique.
#
# Input Format
#
# On the first line of standard input there is an integer representing the number of elements in the list. The second line would contain several space separated integers as the elements of the list.
#
# Constraints
#
# the list elements are unique. list will have more than one element.
#
# Output Format
#
# it should be an integer.

# Sample Input 0
#
# 10
# 1 2 3 4 5 6 7 8 9 10
# Sample Output 0
#
# 9

leng = int((input()))
a = list(map(int, input().split()))
maxi=0
for i in range(1, leng):
    if a[i]>a[maxi]:
        maxi=i
del a[maxi]
maxi=0
for i in range(0, leng-1):
    if a[i]>a[maxi]:
        maxi=i
print(a[maxi])



