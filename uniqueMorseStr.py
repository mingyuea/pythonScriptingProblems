class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-.-....-", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.
        Return the number of different transformations among all words we have.

        Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
        """
        
        morseList = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphlist = list('abcdefghijklmnopqrstuvwxyz')
        morseDict = {alph : morse for alph, morse in zip(alphlist, morseList)}
        morseSet = set()
        for word in words:
            tmpMorse = ''
            for letter in word:
                tmpMorse += morseDict[letter]
            morseSet.add(tmpMorse)
        return len(morseSet)