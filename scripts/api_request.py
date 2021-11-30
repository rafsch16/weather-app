import requests
import configparser
import json

def get_request(city):
    '''
    This function pulls data from openweathermap API

    INPUT
    city - name of a city (str)
    
    OUTPUT 
    data - the requested weather data (json)
    r_status - whether request was succesfull (boolean)
    '''
    # use configparser to read api_key from a config file
    config = configparser.ConfigParser()
    config.read('scripts/apikey.cfg')
    print(config)
    api_key = config['openweathermap']['api_key']

    # assemble url for API request
    url = 'http://api.openweathermap.org/data/2.5/forecast?q=' + city + \
            '&exclude=hourly,minutely,alerts'+'&units=metric' +'&appid=' + api_key 

    # perform GET request
    try:
        r = requests.get(url)
        data = r.json()

    except:
        print('Could not get response')
        data = []
        r_status = False

    # check status of response
    if data['cod'] == '200':
        r_status = True
    else:
        r_status = False

    return r_status, data