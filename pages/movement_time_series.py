import streamlit as st
import utilities
import datasets as db
from pathlib import Path
# from DataBase.CSVDataBase import CSVDataBase


def movement_time_series_page():
    # load data
    # data_dir = Path.cwd() / 'data'
    # print(data_dir)
    # db = CSVDataBase(data_dir)

    df = db.import_static_data()
    totals = df.sum()
    ts = db.get_csse_time_series_deaths()
    ami_w = db.get_apple_movement_indices('walking')
    ami_d = db.get_apple_movement_indices('driving')
    ami_t = db.get_apple_movement_indices('transit')
    n = 15

    # time series movement data
    st.markdown("#### :iphone: walking movement")
    chart = utilities.ami_line_plot(ami_w)
    st.altair_chart(chart)

    st.markdown("#### :blue_car: driving movement\n")
    chart = utilities.ami_line_plot(ami_d)
    st.altair_chart(chart)

    st.markdown("#### :train: transit movement\n")
    chart = utilities.ami_line_plot(ami_t)
    st.altair_chart(chart)

    st.markdown(
        "sources  \n[wikipedia](https://en.wikipedia.org/wiki/Template:2019%E2%80%9320_coronavirus_pandemic_data)  \
        \n[world bank](http://api.worldbank.org/v2/en/indicator/EN.POP.DNST?downloadformat=csv) \
        \n[johns hopkins](https://github.com/CSSEGISandData/COVID-19) \
        \n[apple](https://www.apple.com/covid19/mobility) \
        "
        )


if __name__ == "__main__":
    main()
