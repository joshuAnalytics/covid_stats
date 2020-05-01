# covid_stats
[webapp](https://arcane-lowlands-61640.herokuapp.com/) with live covid-19 stats

## instructions for developers

requirements: python 3

1) clone the repository: 

```bash
$git clone https://github.com/joshuAnalytics/covid_stats.git
```

2) navigate to the repo directory, and install the python library dependencies

```bash
pip install -r requirements.txt
```

3) navigate to the directory, and run:

```
$streamlit run app.py
```

This launches the streamlit web server locally on `http://localhost:8501/` 

You should see a browser window open automatically with a local rendering of the webapp. You can make changes to the code and see the results update in the browser