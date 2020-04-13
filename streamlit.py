import sys
import pandas as pd
import altair as alt
from scraper import get_latest_data
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def get_data():
    df = get_latest_data()
    return df

df = get_data()
# df.style.format("{:,.0f}")
df['death_rate'] = df['deaths'] / df['cases']
totals = df.sum()
n = 10

st.markdown("# Coronavirus pandemic data\n", unsafe_allow_html=False)

#plot deaths
# plot_data = df['deaths'].sort_values(ascending=False).head(n)
# plot_data.sort_values(inplace=True)
# plot = plot_data.plot.barh(title=f"Top {n} by death count")
# plt.gcf().subplots_adjust(bottom=0.1)
# plt.gcf().subplots_adjust(left=0.25)
# st.pyplot()

plot_data = df['deaths'].sort_values(ascending=False).head(n)
plot_data = plot_data.reset_index()[['country','deaths']]
deaths_chart = alt.Chart(plot_data).mark_bar().encode(
    alt.X('country', sort=alt.EncodingSortField(field="country", op="count", order='ascending')),
    alt.Y('deaths')
)
st.altair_chart(deaths_chart)


st.markdown('### data table\n', unsafe_allow_html=False)
st.markdown("click column headers to sort  :arrow_up_small::arrow_down_small:")
st.write(df)

st.write("source: https://en.wikipedia.org/wiki/Template:2019%E2%80%9320_coronavirus_pandemic_data")
