import streamlit as st
from pages import main_stats
from pages import movement_time_series

def page_selector(page):
    if page == 'numbers by country':
        main_stats.main()
    if page == 'global movement over time':
        movement_time_series.main()

#title
st.markdown("# Coronavirus data :earth_asia:\n", unsafe_allow_html=False)

pages = ['numbers by country','global movement over time']
page = st.selectbox('select page',pages,index=0)

page_selector(page)

