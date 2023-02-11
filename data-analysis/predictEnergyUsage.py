from functions import *
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler



def predict_EnergyUsage(dataset) -> np.array:
    year_data = dataset.copy()
    data = year_data
    data = data[~np.all(data == 0, axis=1)]
    df = pd.DataFrame(data)
    scaler = MinMaxScaler(feature_range=(0, 1))
    df_scaled = scaler.fit_transform(df)

    X_train, y_train = [], []
    for i in range(96, df.shape[0]):
        X_train.append(df_scaled[i-96:i, :])
        y_train.append(df_scaled[i, :])

    X_train, y_train = np.array(X_train), np.array(y_train)
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 96))

    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 96)))
    model.add(LSTM(units=50))
    model.add(Dense(96))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(X_train, y_train, epochs=160, batch_size=32)

    inputs = df_scaled[-96:, :]
    inputs = np.reshape(inputs, (1, 96, 96))

    future_data = model.predict(inputs)
    future_data = scaler.inverse_transform(future_data)
    print(np.squeeze(future_data[0, :]))
    plt.plot(np.linspace(0, 96 * 15 / 60, 96), np.squeeze(future_data[0, :]))
    plt.xlabel('Time (hours)')
    plt.ylabel('Energy usage(kwh)')
    plt.title('Prediction')
    plt.show()
    return np.squeeze(future_data[0, :])



