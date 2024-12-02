from resources.leftList import *
from resources.rightList import *
from time import sleep

leftList = sorted(list((leftList)))
rightList = sorted(list((rightList)))

leftLength = len(leftList)
print(f'leftList length = {leftLength}')
rightLength = len(rightList)
print(f'rightList length = {rightLength}')

if leftLength == rightLength:
    print(f'Both lists are of equal length.')

index = 0
distanceTotal = 0
if index <= leftLength:
    while index <= leftLength - 1:
        # print(f'index {index}')
        leftNum = leftList[index]
        rightNum = rightList[index]
        distance = abs(leftNum - rightNum)
        # print(distance)
        distanceTotal += distance
        index +=1

print(f'distanceTotal = {distanceTotal}')