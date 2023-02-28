import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler
from keras.optimizers import Adam


def predict_EnergyUsage(dataset) -> np.array:
    year_data = dataset.copy()
    data = year_data
    data = data[~np.all(data == 0, axis=1)]
    df = pd.DataFrame(data)
    scaler = MinMaxScaler(feature_range=(0, 1))
    df_scaled = scaler.fit_transform(df)

    X_train, y_train = [], []
    for i in range(96, df.shape[0]):
        X_train.append(df_scaled[i - 96:i, :])
        y_train.append(df_scaled[i, :])

    X_train, y_train = np.array(X_train), np.array(y_train)
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 96))

    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True,
              input_shape=(X_train.shape[1], 96)))
    model.add(LSTM(units=50))
    model.add(Dense(96))
    optimizer = Adam(lr=0.005, beta_1=0.9, beta_2=0.999,
                     epsilon=None, amsgrad=False)
    model.compile(loss='mean_squared_error', optimizer=optimizer)
    model.fit(X_train, y_train, epochs=200, batch_size=32)

    inputs = df_scaled[-96:, :]
    inputs = np.reshape(inputs, (1, 96, 96))

    future_data = model.predict(inputs)
    future_data = np.squeeze(scaler.inverse_transform(future_data))
    # plt.plot(np.linspace(0, 96 * 15 / 60, 96), future_data)
    # plt.xlabel('Time (hours)')
    # plt.ylabel('Energy usage(kwh)')
    # plt.title('LSTM Prediction')
    # plt.show()
    return future_data
