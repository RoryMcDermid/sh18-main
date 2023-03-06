# code takes a 2x2 array [[w,x][y,z]] and returns a 1d array with the first value being "none" for no points of high or low power, this is an array with 2 values,
# "min" for a point of low power only, this array has two values
# "max" for a point of high power only, this array has 2 values
# and "both" for a point of high and low power, this array has 3 values
def generate_suggestions(results):
    sentences = [""]

    # this checks if there is a max or min, and if not returns a sentance notifying it
    if results[0] == [-1, -1] and results[1] == [-1, -1]:
        sentences[0] = "none"
        sentences.append("There are no times of especially high or low power usage")
        print(sentences)
        return sentences

    # this if checks if max has returned anything
    if results[0] != [-1, -1]:
        sentences[0] = "max"
        sentences.append(
            "There is a time of high energy between "
            + make_time_string(results[0][0])
            + " and "
            + make_time_string(results[0][1])
            + ", you should attempt to reduce power usage between these times to reduce costs"
        )

    # this if checks if min has returned anything
    if results[1] != [-1, -1]:
        if sentences[0] == "max":
            sentences[0] = "both"
        else:
            sentences[0] = "min"
        sentences.append(
            "There is a time of low energy between "
            + make_time_string(results[1][0])
            + " and "
            + make_time_string(results[1][1])
            + ", well done, having devices running at this time will reduce costs"
        )

    # print(sentances)
    return sentences


def make_time_string(indexIn):
    return str(int(indexIn / 4)) + ":" + str((indexIn % 4) * 15)


# for testing purposes, change suggestions on line 8 to main to allow this file to be run independant of other code
# if __name__ == "__main__":

# main([[-1,-1],[-1,-1]])
