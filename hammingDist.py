class Solution:
    def hammingDistance(self, x, y):
        """
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Input: x = 1, y = 8

Output: 2

Explanation:
1   (0 0 0 1)
8   (1 0 0 0)
The binary results have 2 positions that are different from each other
        """
        
        maxBin = bin(max(x,y))[2:]
        maxLen = len(maxBin)
        minBin = bin(min(x,y))[2:]
        minLen = len(minBin)
        minBin = '0'*(maxLen - minLen) + minBin
        diff = 0
        for maxPos, minPos in zip(maxBin, minBin):
        	if maxPos != minPos:
        		diff += 1

        return diff
        