from loaders import load_from_file
from functions import correct_minimums, calculate_baseline
from plotters import create_multiplot_v2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    sensor_data = load_from_file(sensor_id="6316312")

    df = pd.DataFrame(sensor_data)
    df["values"] = df["values"].map(lambda x: x["pulse_count"])

    # at this point `df` is a dataframe with 34_944 rows (364 days, 96 timepoints)
    # and 2 columns (timestamp: record_date, value: values)

    # -----------

    # `year_data` is a 2D array where each row represents a single day in a year long period
    # and each column represents a timepoint in a day
    year_data = np.reshape(df["values"].values, (364, 96))

    year_data_baseline = calculate_baseline(year_data)
    year_data_corrected = correct_minimums(year_data)

    # -----------
    # plot seasonal data

    winter = np.vstack(year_data_corrected[300:])
    spring = np.zeros((92, 96))
    summer = np.array(year_data_corrected[117:209])
    autumn = np.array(year_data_corrected[209:300])

    _, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))
    datasets = {"winter": winter, "spring": spring, "summer": summer, "autumn": autumn}
    for (title, dataset), ax in zip(datasets.items(), axes.flatten()):
        dataset_baseline = calculate_baseline(dataset)
        create_multiplot_v2(lineplot_data=dataset_baseline, boxplot_data=dataset, title=title, ax=ax)

    plt.tight_layout()
    plt.show()
