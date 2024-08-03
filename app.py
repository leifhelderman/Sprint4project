import streamlit as st
import pandas as pd
import plotly.express as pl
import scipy as sp




df = pd.read_csv('vehicles_us.csv')
model_year_df = df.dropna(subset = ['model_year'])
model_year_df['decade'] = ((model_year_df['model_year'] - 1) / 10).floordiv(1)
model_year_by_decade = model_year_df.groupby('decade').size().reset_index()
odometer_df = df.dropna(subset = ['odometer'])



st.header('Vehicles for sale by Decade')
fig_1 = pl.histogram(model_year_by_decade, x='decade', y=0, nbins = 22)
st.plotly_chart(fig_1, use_container_width=True)

st.header('Price of Vehicle based on Mileage')
fig_2 = pl.scatter(odometer_df, x='odometer', y='price')
st.plotly_chart(fig_2, use_container_width=True)

st.header('Price of Vehicle by Model Year')

check = st.checkbox('Display figure 4')
fig_4 = pl.scatter(model_year_df, x='model_year', y='price')
if check:
    st.write(fig_4)