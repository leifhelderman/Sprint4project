import streamlit as st
import pandas as pd
import plotly_express as pl
import scipy as sp
import numpy as np



df = pd.read_csv('C:\DataScience\Sprint4project/vehicles_us.csv')
model_year_df = df.dropna(subset = ['model_year'])
model_year_df['decade'] = np.floor((model_year_df['model_year'] - 1) / 10) 
model_year_by_decade = model_year_df.groupby('decade').size().reset_index()
odometer_df = df.dropna(subset = ['odometer'])



st.header('Vehicles for sale by Decade')
fig = pl.histogram(model_year_by_decade, x='decade', y=0, nbins = 22)
st.plotly_chart(fig, use_container_width=True)

st.header('Price of Vehicle based on Mileage')
fig = pl.scatter(odometer_df, x='odometer', y='price')
st.plotly_chart(fig, use_container_width=True)

st.header('Price of Vehicle by Model Year')
fig = pl.scatter(model_year_df, x='model_year', y='price')
st.plotly_chart(fig, use_container_width=True)

display_df = st.checkbox('Display dataframe')
df_1 = pd.DataFrame({'Column 1' : [1, 2, 3], 'Column 2': [4, 5, 6]})
if display_df:
    st.write(df_1)