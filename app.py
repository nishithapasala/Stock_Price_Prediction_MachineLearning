import numpy as np 
import pandas as pd 
import yfinance as yf 
import streamlit as st
from tensorflow.keras.models import load_model

model=load_model('/content/drive/MyDrive/Colab Notebooks/stock price prediction project/Stock Predictions Model.keras')

st.header('Stock Market Predictor')

st.text_input('Enter Stock Symbol', 'GOOG')
start = '2012-01-01'
end = '2024-12-31'

data = yf.download(stock, start, end)

st.subheader('Stock Data')
st.write(data)

data_train = pd.DataFrame(data.Close[0:int(len(data)*0.80)])
data_test = pd.DataFrame(data.Close[int(len(data)*0.80):])

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))

pas_100_days = data_train.tail(100)
data_test = pd.concat([pas_100_days,data_train], ignore_index=True)
data_test_scale = scaler.fit_transform(data_test)

x=[]
y=[]
for i in range(100,data_test_scale.shape[0]):
  x.append(data_test_scale[i-100:i])
  y.append(data_test_scale[i,0])


x,y = np.array(x), np.array(y)









