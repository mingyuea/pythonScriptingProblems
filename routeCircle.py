class Solution:
    def judgeCircle(self, moves):
        """

Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.
The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle

Example 1:
Input: "UD"
Output: true
 

Example 2:
Input: "LL"
Output: false
        """
        moveDict = {'U': (1,1), 'D':(1, -1), 'L':(0, -1), 'R':(0, 1)}
        pos = [0, 0]
        for move in moves:
        	pos[moveDict[move][0]] += moveDict[move][1]
        if pos[0] == 0 and pos[1] == 0:
        	return True
        else:
        	return False