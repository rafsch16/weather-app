# Link to Webapp [https://weather-app-rafsch16.herokuapp.com](https://weather-app-rafsch16.herokuapp.com)

# Openweathermap API Data Dashboard 

This is a flask app that visualizes data from the openweathermap API. Data is
pulled directly from the API and then visualized using Plotly.

The flask app from the Udacity Nanodegree Data Scientist program was used as a 
base template and further developed for visualizing openweathermap API data.

## Prerequisites

To install the flask app, you need:
- python3 (python==3.9.7 was used for development)
- python packages in the requirements.txt file
 
 Install the packages with
``` 
 pip install -r requirements.txt
```

## Installing

For Bash use:
'''
$ export FLASK_APP=openweathermap
$ flask run
'''

For CMD use:
'''
> set FLASK_APP=openweathermap
> flask run
'''

For Powershell use:
'''
> $env:FLASK_APP = "openweathermap"
> flask run
'''
