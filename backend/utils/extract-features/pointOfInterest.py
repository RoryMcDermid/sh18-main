


#this code will take an array of a day's worth of readings from combineGraphData.py and return the most important to look into section and the section that is doing best, or if those don't exist return some form of null value
def pointOfInterest(priority ):

    #find the maximum point of the graph
    maxEdges = [-1,-1]
    if(priority[max(priority)] > 0):
        maxEdges = spikeTrough(priority, max(priority), 1)

    #find the minimum point of the graph
    minEdges = [-1,-1]
    if(priority[min(priority)] < 0):
        minEdges = spikeTrough(priority, min(priority), -1)

  

    #return 2d array with [[maxLeftSide, maxRightSide][minLeftSide, minRightSide]], with either being [-1,-1] if there is no max or min
    return [maxEdges, minEdges]


def max(array):

    max = array[0]
    maxPos = 0

    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
            maxPos = i
    return maxPos

def min(array):

    min = array[0]
    minPos = 0

    for i in range(len(array)):
        if array[i] < min:
            min = array[i]
            minPos = i
    return minPos

def difference(current, compare):
    if current == compare:
        return 0
    if current > compare:
        return 1
    #if current < compare, but other situations have been handled so can just return
    return -1

#pointOfInterest is the max/min, direction is whether it is a max (1) or a min (-1)
def spikeTrough(array, pointOfInterest, direction):

    pointLeft = 0
    pointRight = len(array)-1

    for i in range(pointOfInterest, len(array)-1):
        if difference(array[i], array[i+1]) != direction:
            pointRight = i
            break
    for i in reversed(range(1, pointOfInterest)):
        if difference(array[i], array[i-1]) != direction:
            pointLeft = i
            break

    return [pointLeft, pointRight]


#for testing purposes, change pointOfInterest on line 5 to main to allow this file to be run independant of other code
if __name__ == "__main__":
    main([4,3,4,5,4,1,3,-4,-3])