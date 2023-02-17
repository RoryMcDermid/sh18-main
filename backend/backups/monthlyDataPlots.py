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

    mar_22 = np.zeros((31, 96))
    apr_22 = np.zeros((30, 96))
    may_22 = np.zeros((31, 96))
    jun_22 = np.array(year_data[117:147])
    jul_22 = np.array(year_data[147:178])
    aug_22 = np.array(year_data[178:209])
    sep_22 = np.array(year_data[209:239])
    oct_22 = np.array(year_data[239:270])
    nov_22 = np.array(year_data[270:300])
    dec_22 = np.array(year_data[300:331])
    jan_23 = np.array(year_data[331:362])
    feb_23 = np.zeros((28, 96))

    _, axes = plt.subplots(nrows=4, ncols=3, figsize=(10, 10))
    datasets = {
        "December": dec_22,
        "January": jan_23,
        "February": feb_23,
        "March": mar_22,
        "April": apr_22,
        "May": may_22,
        "June": jun_22,
        "July": jul_22,
        "August": aug_22,
        "September": sep_22,
        "October": oct_22,
        "November": nov_22,
    }
    for (title, dataset), ax in zip(datasets.items(), axes.flatten()):
        dataset_baseline = calculate_baseline(dataset)
        dataset_corrected = correct_minimums(dataset)
        create_multiplot_v2(lineplot_data=dataset_baseline, boxplot_data=dataset_corrected, title=title, ax=ax)

    plt.tight_layout()
    plt.show()
