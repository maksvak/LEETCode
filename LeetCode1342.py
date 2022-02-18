'''

Maksim Vakulenko

Leet Code Problem 1342 - Number of steps to reduce to zero

2/18/22


'''


class Solution(object):
    def numberOfSteps(selfself, num):
        steps = 0
        while num != 0:
            if (num % 2) == 0:
                num = num / 2
                steps += 1
                #print('divide by 2 step')
            elif (num % 2) != 0:
                num = num - 1
                steps += 1
                #print('subtract by 1 step')
            else:
                return steps
                print(steps)
        return(steps)


x = input("Enter a number to split: ")
y = int(x)
number = Solution()
print("The number of steps to reduce to 0 is: {}".format(number.numberOfSteps(y)))
