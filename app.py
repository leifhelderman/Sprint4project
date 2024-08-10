import streamlit as st
import pandas as pd
import plotly.express as pl
import scipy as sp




df = pd.read_csv('vehicles_us.csv')
model_year_df = df.copy()
odometer_df = df.copy()
model_year_median = model_year_df['model_year'].median()
odometer_df_median = odometer_df['odometer'].median()
model_year_df['model_year'] = df['model_year'].fillna(model_year_median)
model_year_df['decade'] = ((model_year_df['model_year'] - 1) / 10).floordiv(1)
model_year_by_decade = model_year_df.groupby('decade').size().reset_index()
odometer_df['odometer'] = odometer_df['odomter'].fillna(odometer_df_median)



st.header('Vehicles for sale by Decade')
fig_1 = pl.histogram(model_year_by_decade, x='decade', y=0, nbins = 22)
st.plotly_chart(fig_1, use_container_width=True)

st.header('Price of Vehicle based on Mileage')
fig_2 = pl.scatter(odometer_df, x='odometer', y='price', range_x=(0, 400000), range_y=(0, 150000))
st.plotly_chart(fig_2, use_container_width=True)

st.header('Price of Vehicle by Model Year')

check = st.checkbox('Display figure 4')
fig_4 = pl.scatter(model_year_df, x='model_year', y='price', range_x=(1940, 2020), range_y=(0, 150000))
if check:
    st.write(fig_4)