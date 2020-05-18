import streamlit as st
from pages.main_stats import main_stats_page
from pages.movement_time_series import movement_time_series_page


def page_selector(page):
    if page == 'numbers by country':
        main_stats_page()
    if page == 'global movement over time':
        movement_time_series_page()

# title
st.markdown("# Coronavirus data :earth_asia:\n", unsafe_allow_html=False)

pages = ['numbers by country', 'global movement over time']
page = st.selectbox('select page', pages, index=0)

page_selector(page)
