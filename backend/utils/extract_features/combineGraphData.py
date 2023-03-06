import numpy as np


# averageData is an numpy array of the average for that given day
# predictedData is an numpy array of the next day's prediction
# cost is an numpy array of what power costs when
# all these arrays should be 96 values in length, but data will be handled before this so no need for error handling
def combine_graph_data(averageData, predictedData, cost):
    # priority is what will be returned
    priority = np.array([0] * len(averageData))
    # averageCost is a way to see if an area is "high cost" or "low cost" by seeing if it is above or below the average respectively
    averageCost = np.average(cost)

    for i in range(len(priority)):
        # cost / averageCost to prioritise based on how expensive an area is
        # predictedData - averageData to massively prioritise if an area is higher than it normally is, but not if it is lower
        priority[i] = (predictedData[i] * (cost[i] / averageCost)) * (predictedData[i] - averageData[i])

    # print(priority)

    return priority


# for testing purposes, change combineGraphData on line 8 to main to allow this file to be run independant of other code
# if __name__ == "__main__":

#     main([2,4,3],[3,3,4],[5,5,7])
