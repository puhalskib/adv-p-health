from flask import Flask
from markupsafe import escape
from flask import send_from_directory
from flask import request, render_template
import pandas as pd
import numpy as np
import pickle

with open('./diabetes_automl.pkl', 'rb') as f:
    automl = pickle.load(f)

app = Flask(__name__)

#@app.route("/")
#def predict():
#    return send_from_directory('public/templates', path='index.html')
@app.route("/")
def predict():
    return render_template('index.html')

@app.route('/diabetes', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        #request_data = request.get_json()
        #SEXVAR = request_data['SEXVAR']
        #print(type(pd.DataFrame.from_dict(request.form.copy().to_dict())))
        p = pd.DataFrame(request.form.copy().to_dict(), index=[0])
        #print(pd.DataFrame(request.form.copy().to_dict(), index=[0]))
        #print(type(pd.DataFrame(request.form.copy().to_dict(), index=[0])))
        #print(pd.DataFrame(request.form.copy().to_dict(), index=[0]).describe())
        #print(type(request.form.copy().to_dict()))
        #print(pd.DataFrame.from_dict(request.form.copy().to_dict()))
        #print(request.form.copy().to_dict())
        #SEXVAR = request.form.get('SEXVAR')
        #GENHLTH = request.form.get('GENHLTH')
        #PHYSHLTH = request.form.get('PHYSHLTH')
        #MENTHLTH = request.form.get('MENTHLTH')
        #p = pd.read_csv('./test_row.csv')
        p.to_csv('./input_test.csv')
        #framework = request.form.get('framework')
        #return "prediction {}.".format(automl.predict(p))
        return p.to_string()
        #'''
        #    <h1>The SEXVAR value is: {}</h1>
        #    <h1>The GENHLTH value is: {}</h1>
        #    <h1>The PHYSHLTH value is: {}</h1>
        #    <h1>The MENTHLTH value is: {}</h1>'''.format(SEXVAR, GENHLTH, PHYSHLTH, MENTHLTH)

    # otherwise handle the GET request
    return send_from_directory('templates', path='diabetes.html')

#app.run(port=5000)
