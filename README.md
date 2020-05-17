# covid_stats
[webapp](https://arcane-lowlands-61640.herokuapp.com/) with live covid-19 stats

This is a community-led project focused on providing insighful and innovative data visualisations relating to the ongoing coronavirus pandemic. The community has a plethora of different expertise including policy research, data analytics and software development. 

The goal is to: 
* explore ideas for data visualisation and analysis, 
* realise these ideas as dynamic and interactive data visualisations, 
* get feedback from the community, continuing to develop the app

Ultimately we may wish to share the app more broadly. 

## where to start

* join the discussion on [slack](http://covid-19-data-vis.slack.com)
* check the [issues page](https://github.com/joshuAnalytics/covid_stats/issues)
* view the current items on the [project kanban](https://github.com/joshuAnalytics/covid_stats/projects/1)

## how to contribute code

* the app is running purely in python, using a library called [streamlit](https://streamlit.io). No javascript or css required! 
* you can add a new page to the website simply by creating a new standalone module - see [here](https://github.com/joshuAnalytics/covid_stats/tree/master/pages) for examples.
* each page is referenced in the `app.py` so that it can be browsed via  dropdown menu
* the `DataSets` class is used for all data retrival and preprocessing steps

## how to run the app locally 

requirements: [python 3](https://www.python.org/downloads/)

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