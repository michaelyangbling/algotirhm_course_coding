# Devise an algorithm which for an number (not necessarily an integer!) , finds an approximation of  such that   The number of operations that your algorithm do should be .
#
# Clearly you are not allowed to use Math library in your programming language.
#
# Input Format
#
# The first line of the input consists of a number  .
#
# Constraints: 0<=N<=1000000
#
#
#
# Output Format
#
# print out the number that you have a calculated to STDOUT.
#
# Sample Input 0
#
# 25
# Sample Output 0
#
# 5

#this algorithm resembles binary search, so when n>1, the worst number of operations is: O(lg(n))
#when n<=1, number of operations is limited
#so the worst  time complexity is O(lg(n))
#the space complexity can be constant since we can only use several variables
n=float(input())
if n==0:
    q=0
elif n==1:
    q=1
elif n>1:
    q=(1+n)/2;lower=1;upper=n
    while True:
        if q*q-n>-0.01 and q*q-n<0.01:
            break
        elif q*q-n<=-0.01:
            lower=q;q=(lower+upper)/2
        else:
            upper=q;q=(lower+upper)/2
elif n<1:
    q=(1+n)/2;lower=n;upper=1
    while True:
        if q*q-n>-0.01 and q*q-n<0.01:
            break
        elif q*q-n<=-0.01:
            lower=q;q=(lower+upper)/2
        else:
            upper=q;q=(lower+upper)/2
print(q)