class Solution:
    def peakIndexInMountainArray( A):
        """
Let's call an array A a mountain if the following properties hold:
A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array A, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1], or return
False if A is not a mountain.

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a list
        """

        leftBool = True
        rightBool = True
        peakInd = None
        if len(A) < 3:
        	return False
        for ind, val in enumerate(A):
        	if ind != 0 and ind != len(A) - 1 and A[ind - 1] < val and A[ind + 1] < val:
        		peakInd = ind
        		break
        if(peakInd):
        	for ind, val in enumerate(A):
        		if ind < peakInd and A[ind - 1] >= val and ind != 0:
        			leftBool = False
        			break
        		if ind > peakInd and ind < len(A) - 1 and A[ind + 1] >= val:
        			rightBool = False
        			break
        	if leftBool and rightBool:
        		return peakInd
        	else: 
        		return False
        else:
        	return False

print(Solution.peakIndexInMountainArray([0,1,4,2]))