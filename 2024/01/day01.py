from resources.leftList import *
from resources.rightList import *

# Part 1
def distance(list1, list2):
    list1 = sorted(list((list1)))
    list2 = sorted(list((list2)))

    leftLength = len(list1)
    rightLength = len(list2)
    
    if leftLength == rightLength:
        
        index = 0
        distanceTotal = 0
        if index <= leftLength:
            while index <= leftLength - 1:
                # print(f'index {index}')
                leftNum = list1[index]
                rightNum = list2[index]
                distance = abs(leftNum - rightNum)
                # print(distance)
                distanceTotal += distance
                index +=1

        return distanceTotal
    
    else:
        print(f'Lists are not of equal length.')


testResults = distance(test_leftList, test_rightList)
if testResults == 11:
    print(f'Test passed!')
    distanceTotal = distance(leftList, rightList)
    print(f'distanceTotal = {distanceTotal}')
else: 
    print(f'Test faiiled!')