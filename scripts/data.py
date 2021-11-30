import pandas as pd
import numpy as np
import plotly.graph_objs as go
from datetime import datetime
from scripts.api_request import get_request

# function to get the data and prepare the figures 
def return_figures(city_names):
    """Returns six plotly visualizations using indicator data from the openweathermap API

    # Example of the openweathermap API endpoint:
    # http://api.openweathermap.org/data/2.5/forecast?q={city name},{country code}&appid={API key}

    INPUT
    cities_names - cities for filtering the data (list)

    OUTPUT
    figures - list containing the four plotly visualizations (dict)
    """

    data_frames = []

   
    for city in city_names:

        # pull data from openweathermap API
        r_status, data = get_request(city)

        # stores the indicator data of interest
        data_frames.append(data)

    # creat the garph one
    graph_one = []
    
    for i in range(len(city_names)):
        df_one = pd.DataFrame(data_frames[i]['list'])
        x_t = df_one.dt.tolist()
        x_val =  []
        y_val =  []
        for j in range(df_one.main.shape[0]):
            x_val.append(datetime.utcfromtimestamp(x_t[j]).strftime('%Y-%m-%d %H:%M:%S'))
            y_val.append(df_one.main[j]['temp'])
        graph_one.append(
            go.Scatter(
            x = x_val,
            y = y_val,
            mode = 'lines',
            name = city_names[i]
            )
        )

    layout_one = dict(
                xaxis = dict(tickformat = '%d %b %H:%M'),
                yaxis = dict(title = {'text': 'Temperature (°C)', 'font': {'size': 16}}),
                images = [dict(source = "/static/img/temperature.png",
                                xref = "paper",
                                yref = "paper",
                                x = 0,
                                y = 1,
                                sizex = 0.3,
                                sizey = 0.3,
                                xanchor = "right",
                                yanchor = "bottom")],
                )

    # creat the garph two
    graph_two = []
    
    for i in range(len(city_names)):
        df_two = pd.DataFrame(data_frames[i]['list'])
        x_t = df_two.dt.tolist()
        x_val =  []
        y_val =  []
        for j in range(df_two.main.shape[0]):
            x_val.append(datetime.utcfromtimestamp(x_t[j]).strftime('%Y-%m-%d %H:%M:%S'))

            try:
                if type(df_two.rain[j])==type({0: 0}):
                    y_val.append(df_two.rain[j]['3h'])
                else:
                    y_val.append(0.0)
            except:
                y_val = [0] * len(x_val)

        
        graph_two.append(
            go.Scatter(
            x = x_val,
            y = y_val,
            mode = 'lines',
            name = city_names[i]
            )
        )

    layout_two = dict(
                xaxis = dict(tickformat = '%d %b %H:%M'),
                yaxis = dict(title = {'text': 'Rain volume last 3h (mm)', 'font': {'size': 16}}),
                images = [dict(source = "/static/img/rain.png",
                                xref = "paper",
                                yref = "paper",
                                x = 0,
                                y = 1,
                                sizex = 0.3,
                                sizey = 0.3,
                                xanchor = "right",
                                yanchor = "bottom")],
                )

    # creat the garph three
    graph_three = []
    
    for i in range(len(city_names)):
        df_three = pd.DataFrame(data_frames[i]['list'])
        x_t = df_three.dt.tolist()
        x_val =  []
        y_val =  []
        for j in range(df_three.main.shape[0]):
            x_val.append(datetime.utcfromtimestamp(x_t[j]).strftime('%Y-%m-%d %H:%M:%S'))
            y_val.append(df_three.clouds[j]['all'])
        graph_three.append(
            go.Scatter(
            x = x_val,
            y = y_val,
            mode = 'lines',
            name = city_names[i]
            )
        )

    layout_three = dict(
                xaxis = dict(tickformat = '%d %b %H:%M'),
                yaxis = dict(title = {'text': 'Cloudiness (%)', 'font': {'size': 16}}),
                images = [dict(source = "/static/img/cloudiness.png",
                                xref = "paper",
                                yref = "paper",
                                x = 0,
                                y = 1,
                                sizex = 0.3,
                                sizey = 0.3,
                                xanchor = "right",
                                yanchor = "bottom")],
                )

    # creat the garph four
    graph_four = []
    
    for i in range(len(city_names)):
        df_four = pd.DataFrame(data_frames[i]['list'])
        x_t = df_four.dt.tolist()
        x_val =  []
        y_val =  []
        for j in range(df_four.main.shape[0]):
            x_val.append(datetime.utcfromtimestamp(x_t[j]).strftime('%Y-%m-%d %H:%M:%S'))
            try:
                if type(df_four.snow[j])==type({0: 0}):
                    y_val.append(df_four.snow[j]['3h'])
                else:
                    y_val.append(0.0)
            except:
                y_val = [0] * len(x_val)

        graph_four.append(
            go.Scatter(
            x = x_val,
            y = y_val,
            mode = 'lines',
            name = city_names[i]
            )
        )

    layout_four = dict(
                xaxis = dict(tickformat = '%d %b %H:%M'),
                yaxis = dict(title = {'text': 'Snow volume last 3h (mm)', 'font': {'size': 16}}),
                images = [dict(source = "/static/img/snow.png",
                                xref = "paper",
                                yref = "paper",
                                x = 0,
                                y = 1,
                                sizex = 0.3,
                                sizey = 0.3,
                                xanchor = "right",
                                yanchor = "bottom")],
                )

    # creat the garph five
    graph_five = []
    
    for i in range(len(city_names)):
        df_five = pd.DataFrame(data_frames[i]['list'])
        x_t = df_five.dt.tolist()
        x_val =  []
        y_val =  []
        for j in range(df_five.main.shape[0]):
            x_val.append(datetime.utcfromtimestamp(x_t[j]).strftime('%Y-%m-%d %H:%M:%S'))
            y_val.append(df_five.wind[j]['speed'])
        graph_five.append(
            go.Scatter(
            x = x_val,
            y = y_val,
            mode = 'lines',
            name = city_names[i]
            )
        )

    layout_five = dict(
                xaxis = dict(tickformat = '%d %b %H:%M'),
                yaxis = dict(title = {'text': 'Wind speed (m/s)', 'font': {'size': 16}}),
                images = [dict(source = "/static/img/wind.png",
                                xref = "paper",
                                yref = "paper",
                                x = 0,
                                y = 1,
                                sizex = 0.3,
                                sizey = 0.3,
                                xanchor = "right",
                                yanchor = "bottom")],
                )

    # creat the garph six
    graph_six = []
    
    for i in range(len(city_names)):
        df_six = pd.DataFrame(data_frames[i]['list'])
        x_t = df_six.dt.tolist()
        x_val =  []
        y_val =  []
        for j in range(df_six.main.shape[0]):
            x_val.append(datetime.utcfromtimestamp(x_t[j]).strftime('%Y-%m-%d %H:%M:%S'))
            y_val.append(df_six.main[j]['humidity'])
        graph_six.append(
            go.Scatter(
            x = x_val,
            y = y_val,
            mode = 'lines',
            name = city_names[i]
            )
        )

    layout_six = dict(
                xaxis = dict(tickformat = '%d %b %H:%M'),
                yaxis = dict(title = {'text': 'Humidity (%)', 'font': {'size': 16}}),
                images = [dict(source = "/static/img/humidity.png",
                                xref = "paper",
                                yref = "paper",
                                x = 0,
                                y = 1,
                                sizex = 0.25,
                                sizey = 0.25,
                                xanchor = "right",
                                yanchor = "bottom")],
                )

    # append all charts
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))
    figures.append(dict(data=graph_five, layout=layout_five))
    figures.append(dict(data=graph_six, layout=layout_six))
    
    return figures



