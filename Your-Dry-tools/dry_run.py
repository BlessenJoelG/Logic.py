"""Input: num = 30
Output: 14
Explanation:
The 14 integers less than or equal to 30 whose digit sums are even are
2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28."""
num,c = int(input()),0
for a in range(1,num+1):
    if sum(int(x) for x in str(a))%2 == 0:
        c += 1
print(c)