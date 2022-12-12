import pandas as pd
import streamlit as st

# read data in pandas dataframe
df_train = pd.read_csv('test.csv', nrows=10_000, parse_dates=["pickup_datetime"])

# list first few rows (datapoints)
df_train.head()
cords_take_df = df_train[["pickup_longitude", "pickup_latitude"]].copy()
cords_take_df.rename(columns={"pickup_longitude": 'lon', "pickup_latitude": 'lat'}, inplace=True)
cords_drop_df = df_train[["dropoff_longitude", "dropoff_latitude"]].copy()
cords_drop_df.rename(columns={"dropoff_longitude": 'lon', "dropoff_latitude": 'lat'}, inplace=True)
passenger_df = df_train["passenger_count"].copy()

st.write(":raising_hand: City pickup map :taxi:")
st.map(cords_take_df)
st.write(":raising_hand: City drop off map :taxi:")
st.map(cords_drop_df)
st.bar_chart(passenger_df)
st.dataframe(df_train)
