from weatherapp import app

from flask import render_template, request
import plotly
import json
import pickle
from scripts.data import return_figures
from scripts.api_request import get_request

# create lists for dafault and selected cities
cities_selected = []
cities_default = ['Wädenswil,CH','Horgen,CH','Olten,CH','Riehen,CH','Sargans,CH','Köniz,CH',
        'Zermatt,CH','St. Moritz,CH','Romanshorn,CH', 'Altdorf,CH','Embrach,CH',
        'Delémont,CH','Interlaken,CH','Bellinzona,CH','Visp,CH','Nyon,CH']

# pickle dump the lists for default and selected cities
with open('cities_selected.pkl', 'wb') as f1:
    pickle.dump(cities_selected, f1)
with open('cities_default.pkl', 'wb') as f2:
    pickle.dump(cities_default, f2)

@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():

    # get a list of the figures and layouts
    # first pickle load the lists for default and selected cities
    with open('cities_selected.pkl', 'rb') as f1:
        cities_selected = pickle.load(f1)
    with open('cities_default.pkl', 'rb') as f2:
        cities_default = pickle.load(f2)

    # Parse the POST request cities lists
    if (request.method == 'POST') and request.form:

        # pickle load selected cities
        with open('cities_selected.pkl', 'rb') as f1:
            cities_selected = pickle.load(f1)

        # retrieve user input
        req=request.form

        # append new_city from text input form to cities_selected
        if list(req.keys())[0] == 'new_city':
            
            req_form=list(req.values())

            # check if new_city is valid
            r_status, data = get_request(req_form[0])
            
            # add valid new_city to cities_selected 
            if r_status:
                
                cities_selected.append(req_form[0])
                cities_selected = list(sorted(set(cities_selected), key=cities_selected.index))
                
                # pickle dump selected cities
                with open('cities_selected.pkl', 'wb') as f1:
                    pickle.dump(cities_selected, f1)
            else:
                req_form = False
            
        # create cities_selected from checked boxes in form
        else:

            req_form = list(req.keys())
            cities_selected = []

            for city in req_form:
                cities_selected.append(city)
            
            cities_selected = list(sorted(set(cities_selected), key=cities_selected.index))

            # pickle dump selected cities
            with open('cities_selected.pkl', 'wb') as f1:
                pickle.dump(cities_selected, f1)

        # GET request returns figures for selected citties
        figures = return_figures(cities_selected)

        # Append selected cites to default cities
        if req_form:

            for city in req_form:

                cities_default.append(city)
                
                cities_default = list(sorted(set(cities_default), key=cities_default.index))
                
                # pickle dump default cities
                with open('cities_default.pkl', 'wb') as f2:
                    pickle.dump(cities_default, f2)
    
    # GET request returns all figures for initial page load
    else:

        figures = return_figures([cities_default[0]])
        
        cities_selected = []

        # add initial cities to cities_selected
        cities_selected.append(cities_default[0])#[1])

        # pickle dump selected cities
        with open('cities_selected.pkl', 'wb') as f1:
                pickle.dump(cities_selected, f1)
    
    # list ids for the html id tag
    ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]
	
    # Convert the plotly figures to JSON for javascript in html template
    figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

    # render the template
    return render_template('index.html', ids=ids, figuresJSON=figuresJSON,
		all_cities=cities_default,
		cities_selected=cities_selected)

#if __name__ == '__main__':
#    app.run()
