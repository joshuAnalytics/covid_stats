import sys
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import altair as alt
#custom methods
from utilities import bar_chart,scatter_plot
import datasets

#load data
df = datasets.import_static_data()
totals = df.sum()
n = 10

#title
st.markdown("# Coronavirus data :earth_asia:\n", unsafe_allow_html=False)
st.markdown(f":skull: reported deaths: `{totals['deaths']:,.0f}` ")
st.markdown(f":male_zombie: reported recoveries: `{totals['recov']:,.0f}`  \n")
st.markdown(f":face_with_thermometer: reported cases: `{totals['cases']:,.0f}` ")
st.markdown("  \n  \n  \n  \n")

#top n bar plots
chart = bar_chart(df,'country','deaths',n=n)
st.altair_chart(chart)
chart = bar_chart(df,'country','cases',n=n)
st.altair_chart(chart)

scatter = scatter_plot(df,'cases_per_million','pop_density','country',10)
st.altair_chart(scatter)

#data table
st.markdown('### data table\n', unsafe_allow_html=False)
st.markdown("*click column headers to sort*  :arrow_up_small::arrow_down_small:")
formatted_df = df.style.format({"cases": "{:,.0f}", "deaths": "{:,.0f}", "recov": "{:,.0f}"})
st.write(formatted_df)

st.markdown("sources  \n[wikipedia](https://en.wikipedia.org/wiki/Template:2019%E2%80%9320_coronavirus_pandemic_data)  \n[world bank](http://api.worldbank.org/v2/en/indicator/EN.POP.DNST?downloadformat=csv)")