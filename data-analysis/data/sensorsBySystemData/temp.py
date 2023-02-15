import json
from loaders import load_from_file
from functions import correct_minimums, calculate_baseline
from plotters import create_multiplot_v2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    with open("data/sensorsBySystemData/sensorsBySystemData.json") as f:
        data_dict = json.load(f)

    dataframes = {}
    for system in data_dict.keys():
        dataframes[str(system)] = pd.DataFrame.from_dict(data_dict[system])

    print(dataframes["2542"].head())


if __name__ == "__main__":
    main()
