import matplotlib.pyplot as plt

def create_multiplot(lineplot_data, boxplot_data):
    _, ax = plt.subplots()
    ax.plot(lineplot_data)
    ax.boxplot(boxplot_data)

    timestamps = ["{:02d}:{:02d}".format(i//4, (i%4)*15) for i in range(96)]
    ax.set_xticklabels(timestamps, fontsize=6)
    plt.xticks(rotation=-90)

    plt.show()