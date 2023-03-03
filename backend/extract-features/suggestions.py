


#code takes a 2x2 array [[w,x][y,z]] and returns a 1d array with the first value being "none" for no points of high or low power, this is an array with 2 values,
#"min" for a point of low power only, this array has two values
#"max" for a point of high power only, this array has 2 values
# and "both" for a point of high and low power, this array has 3 values
def suggestions(results):

    sentances = [""]

    #this checks if there is a max or min, and if not returns a sentance notifying it
    if results[0] == [-1,-1] and results[1] == [-1,-1]:
        sentances[0] = "none"
        sentances.append("There are no times of especially high or low power usage")
        print(sentances)
        return sentances
    
    #this if checks if max has returned anything
    if results[0] != [-1,-1]:
        sentances[0] = "max"
        sentances.append("There is a time of high energy between " + time(results[0][0]) + " and " + time(results[0][1]) + ", you should attempt to reduce power usage between these times to reduce costs")

    #this if checks if min has returned anything
    if results[1] != [-1,-1]:
        if sentances[0] == "max":
            sentances[0] = "both"
        else:
            sentances[0] = "min"
        sentances.append("There is a time of low energy between " + time(results[1][0]) + " and " + time(results[1][1]) + ", well done, having devices running at this time will reduce costs")

    print(sentances)
    return sentances

def time(indexIn):
    return str(int(indexIn/4)) + ":" + str((indexIn % 4) * 15)

#for testing purposes, change suggestions on line 8 to main to allow this file to be run independant of other code
# if __name__ == "__main__":

    # main([[-1,-1],[-1,-1]])