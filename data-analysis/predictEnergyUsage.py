import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def predict_EnergyUsage(dataset) -> np.array:
    year_data = dataset.copy()
    data = year_data

    data = data[~np.all(data == 0, axis=1)]

    df = pd.DataFrame(data)

    samples = []
    for i in range(df.shape[0]):
        sample = []
        for j in range(df.shape[1]):
            sample.append(df.iloc[i, j])
        samples.append(sample)

    df = df.iloc[:, :]
    samples = np.array(samples)
    samples = samples[:-1, :]

    X_train, X_test, y_train, y_test = train_test_split(samples, df.shift(-1).dropna(), test_size=0.1, random_state=0)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)
    print("score：", score)

    future_data = model.predict(X_test[-1].reshape(1, -1))
    print("predict:", future_data)
