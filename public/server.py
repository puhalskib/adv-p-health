from flask import Flask
from markupsafe import escape
from flask import send_from_directory
from flask import request, render_template

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
        SEXVAR = request.form.get('SEXVAR')
        GENHLTH = request.form.get('GENHLTH')
        PHYSHLTH = request.form.get('PHYSHLTH')
        MENTHLTH = request.form.get('MENTHLTH')
        #framework = request.form.get('framework')
        return '''
            <h1>The SEXVAR value is: {}</h1>
            <h1>The GENHLTH value is: {}</h1>
            <h1>The PHYSHLTH value is: {}</h1>
            <h1>The MENTHLTH value is: {}</h1>'''.format(SEXVAR, GENHLTH, PHYSHLTH, MENTHLTH)

    # otherwise handle the GET request
    return send_from_directory('templates', path='diabetes.html')

#app.run(port=5000)
