class Solution:
    def fizzBuzz( n):
        """
Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
        
Example:

n = 15,
Return: ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
        """
        fizzInd = {x for x in range(0, n+1, 3)}
        buzzInd = {x for x in range(0, n+1, 5)}
        fbInd = fizzInd & buzzInd

        fizzInd = fizzInd - fbInd
        buzzInd = buzzInd - fbInd

        numList = [str(num) for num in range(0, n+1)]
        for ind in fizzInd:
        	numList[ind] = "Fizz"
        for ind in buzzInd:
        	numList[ind] = "Buzz"
        for ind in fbInd:
        	numList[ind] = "FizzBuzz"

        return numList[1:]

print(Solution.fizzBuzz(15))