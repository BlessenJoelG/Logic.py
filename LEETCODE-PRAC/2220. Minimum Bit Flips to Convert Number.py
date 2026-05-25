class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        width,c = max(start.bit_length(),goal.bit_length()),0
        start = format(start,f"0{width}b")
        goal = format(goal,f"0{width}b")
        for i in range(len(start)):
            if start[i] != goal[i]:
                c += 1
        return c