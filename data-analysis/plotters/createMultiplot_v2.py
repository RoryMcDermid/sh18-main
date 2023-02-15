import matplotlib.pyplot as plt


def create_multiplot_v2(lineplot_data, boxplot_data, title="", ax=None):
    if ax is None:
        _, ax = plt.subplots()
    ax.plot(lineplot_data)
    ax.boxplot(boxplot_data)

    timestamps = []
    # timestamps = ["{:02d}:{:02d}".format(i // 4, (i % 4) * 15) for i in range(96)]
    ax.set_xticklabels(timestamps, fontsize=6)
    ax.set_title(title, fontsize=16)
    return ax
