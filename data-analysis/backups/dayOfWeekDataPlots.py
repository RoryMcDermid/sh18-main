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

    # -----------
    # plot seasonal data

    mon = year_data[6::7]
    tue = year_data[0::7]
    wed = year_data[1::7]
    thu = year_data[2::7]
    fri = year_data[3::7]
    sat = year_data[4::7]
    sun = year_data[5::7]

    _, axes = plt.subplots(nrows=3, ncols=3, figsize=(10, 10))
    datasets = {
        "mon": mon,
        "tue": tue,
        "wed": wed,
        "thu": thu,
        "fri": fri,
        "sat": sat,
        "sun": sun,
    }
    for (title, dataset), ax in zip(datasets.items(), axes.flatten()):
        dataset_baseline = calculate_baseline(dataset)
        dataset_corrected = correct_minimums(dataset)
        create_multiplot_v2(lineplot_data=dataset_baseline, boxplot_data=dataset_corrected, title=title, ax=ax)

    plt.tight_layout()
    plt.show()
