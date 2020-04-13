import sys
import pandas as pd
import altair as alt
from scraper import get_latest_data
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

#get data
df = get_latest_data()
n = 20

st.markdown("# Coronavirus pandemic data\n", unsafe_allow_html=False)

#plot deaths
plot_data = df['deaths'].sort_values(ascending=False).head(n)
plot_data.sort_values(inplace=True)
plot = plot_data.plot.barh(title=f"Top {n} by death count")
plt.gcf().subplots_adjust(bottom=0.1)
plt.gcf().subplots_adjust(left=0.25)
st.pyplot()


st.markdown('## top 10 countries\n', unsafe_allow_html=False)
st.write(df.head(10))

st.markdown("source: https://en.wikipedia.org/wiki/Template:2019%E2%80%9320_coronavirus_pandemic_data")
