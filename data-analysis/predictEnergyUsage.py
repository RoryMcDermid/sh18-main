import numpy as np


def predict_EnergyUsage(dataset) -> np.array:
    year_data = dataset.copy()
    year_data[year_data == 0] = np.nan
    weeks_data = year_data.reshape(52, 7, 96)
    diff_ratio_first4 = np.empty(shape=(0, 96))
    #diff_ratio_last4 = np.empty(shape=(0, 96))

    for i1 in range(51):
        i2 = i1 + 1
        diff_ratio1 = (weeks_data[i2, 0, :] - weeks_data[i1, 6, :]) /weeks_data[i1, 6, :]
        diff_ratio_first4 = np.append(diff_ratio_first4, diff_ratio1.reshape(1, -1), axis=0)

    #for i1 in range(43, 50):
    #    i2 = i1 + 1
    #    diff_ratio2 = (weeks_data[i2, 0, :] - weeks_data[i1, 6, :]) #/ weeks_data[i1, 6, :]
    #    diff_ratio_last4 = np.append(diff_ratio_last4, diff_ratio2.reshape(1, -1), axis=0)

    #diff_ratio = np.append(diff_ratio_first4, diff_ratio_last4, axis=0)
    mean_ratio = np.nanmean(diff_ratio_first4, axis=0)
    today_predict = weeks_data[51, 6, :] + mean_ratio

    return today_predict
