import sys
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import altair as alt
#custom methods
import utilities
import datasets

def main():
    
    #load data
    df = datasets.import_static_data()
    totals = df.sum()
    ts = datasets.get_csse_time_series_deaths()
    ami_w = datasets.get_apple_movement_indices('walking')
    ami_d = datasets.get_apple_movement_indices('driving')
    ami_t = datasets.get_apple_movement_indices('transit')
    n = 15

    #time series movement data
    st.markdown(f"#### :iphone: walking movement")
    chart = utilities.ami_line_plot(ami_w)
    st.altair_chart(chart)
    
    st.markdown(f"#### :blue_car: driving movement\n")
    chart = utilities.ami_line_plot(ami_d)
    st.altair_chart(chart)
    
    st.markdown(f"#### :train: transit movement\n")
    chart = utilities.ami_line_plot(ami_t)
    st.altair_chart(chart)

    st.markdown("sources  \n[wikipedia](https://en.wikipedia.org/wiki/Template:2019%E2%80%9320_coronavirus_pandemic_data)  \
                \n[world bank](http://api.worldbank.org/v2/en/indicator/EN.POP.DNST?downloadformat=csv) \
                \n[johns hopkins](https://github.com/CSSEGISandData/COVID-19) \
                \n[apple](https://www.apple.com/covid19/mobility) \
                ")
    
if __name__ == "__main__":
    main()