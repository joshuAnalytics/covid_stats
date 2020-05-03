import sys
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import altair as alt
#custom methods
import utilities
import datasets

#load data
df = datasets.import_static_data()
totals = df.sum()
ts = datasets.get_csse_time_series_deaths()
ami_w = datasets.get_apple_movement_indices('walking')
ami_d = datasets.get_apple_movement_indices('driving')
ami_t = datasets.get_apple_movement_indices('transit')
n = 15

def plot_simple_chart(icon, title, data_type, dataframe):
    st.markdown(f"#### :{icon}: {title}\n")
    st.markdown(f"  \n  \n  \n  \n  \n")
    if data_type == 'aline':
        chart = utilities.ami_line_plot(dataframe)
    else:
        return
    return st.altair_chart(chart)

#title
st.markdown("# Coronavirus data :earth_asia:\n", unsafe_allow_html=False)
st.markdown(f":skull: reported deaths: `{totals['deaths']:,.0f}` ")
st.markdown(f":male_zombie: reported recoveries: `{totals['recov']:,.0f}`  \n")
st.markdown(f":face_with_thermometer: reported cases: `{totals['cases']:,.0f}` ")
st.markdown("  \n  \n  \n  \n")

#time series movement data
plot_simple_chart('iphone','walking around','aline',ami_w)
plot_simple_chart('blue_car','driving movement','aline',ami_d)
plot_simple_chart('train','transit movement','aline',ami_t)

#time series deaths plot
st.markdown(f"#### :skull: deaths over time\n")
st.markdown(f"  \n  \n  \n  \n  \n")
countries = ['United Kingdom','Spain','US','Italy','France']
all_countries = ts['country'].unique().tolist()
# st.sidebar.multiselect('select countries', all_countries, default=countries)
chart = utilities.line_plot(ts,countries)
st.altair_chart(chart)

#bar plots
chart = utilities.bar_chart(df,'country','deaths',n=n)
st.altair_chart(chart)
chart = utilities.bar_chart(df,'country','cases',n=n)
st.altair_chart(chart)

#scatter plot
scatter = utilities.scatter_plot(df,'cases_per_million','pop_density','country',n)
st.altair_chart(scatter)

#data table
pd.set_option('display.max_colwidth', -1)
st.markdown('### data table\n', unsafe_allow_html=False)
st.markdown("*click column headers to sort*  :arrow_up_small::arrow_down_small:")
formatted_df = df.style.format({"cases": "{:,.0f}", "deaths": "{:,.0f}", "recov": "{:,.0f}"})
st.write(formatted_df)

st.markdown("sources  \n[wikipedia](https://en.wikipedia.org/wiki/Template:2019%E2%80%9320_coronavirus_pandemic_data)  \
            \n[world bank](http://api.worldbank.org/v2/en/indicator/EN.POP.DNST?downloadformat=csv) \
            \n[johns hopkins](https://github.com/CSSEGISandData/COVID-19) \
            \n[apple](https://www.apple.com/covid19/mobility) \
            ")