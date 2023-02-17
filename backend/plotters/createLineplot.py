import matplotlib.pyplot as plt

def create_lineplot(datapoints):
    _, ax = plt.subplots()
    ax.plot(datapoints)

    timestamps = ["{:02d}:{:02d}".format(i//4, (i%4)*15) for i in range(96)]
    ax.set_xticklabels(timestamps, fontsize=6)
    plt.xticks(rotation=-90)
    
    plt.show()

    