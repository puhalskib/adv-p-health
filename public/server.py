from flask import Flask
from markupsafe import escape
from flask import send_from_directory
from flask import request, render_template
import pandas as pd
import numpy as np
import pickle

with open('../models/diabetes_automl_2.pkl', 'rb') as f:
    automl = pickle.load(f)

with open('../models/heart_automl.pkl', 'rb') as f:
    heartml = pickle.load(f)

app = Flask(__name__)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

#@app.route("/")
#def predict():
#    return send_from_directory('public/templates', path='index.html')
@app.route("/")
def predict():
    return render_template('index.html')

@app.route('/heart', methods=['GET', 'POST'])
def heart_form():
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
        p = p.astype(float)
        #p.to_csv('./input_test.csv')
        #framework = request.form.get('framework')
        #return "prediction {}.".format(automl.predict(p))

        #begin conversion to trained dataframe
        # BPHIGH6
        p['high_blood_pressure'] = p['BPHIGH6']
        p['high_blood_pressure'].replace([0,1,2],0, inplace=True)
        p['high_blood_pressure'].replace(3,1, inplace=True)
        p['pregnant_high_blood_pressure'] = p['BPHIGH6']
        p['pregnant_high_blood_pressure'].replace([0,1,3],0, inplace=True)
        p['pregnant_high_blood_pressure'].replace(2,1, inplace=True)
        p['borderline_high_blood_pressure'] = p['BPHIGH6']
        p['borderline_high_blood_pressure'].replace([0,2,3],0, inplace=True)
        p = p.drop(['BPHIGH6'], axis=1)

        #CHOLCHK3
        p['cholesterol_checked_within_year'] = p['CHOLCHK3']
        p = p.drop(['CHOLCHK3'], axis=1)

        #MARITAL
        p['married'] = p['MARITAL']
        p['married'].replace([1,2,3,4,5],2, inplace=True)
        p['married'].replace(0,1, inplace=True)
        p['married'].replace(2,0, inplace=True)
        p['divorced'] = p['MARITAL']
        p['divorced'].replace([0,2,3,4,5],0, inplace=True)
        p['widowed'] = p['MARITAL']
        p['widowed'].replace([1,3,4,5],0, inplace=True)
        p['widowed'].replace(2,1, inplace=True)
        p['separated'] = p['MARITAL']
        p['separated'].replace([1,2,4,5],0, inplace=True)
        p['separated'].replace(3,1, inplace=True)
        p['never_married'] = p['MARITAL']
        p['never_married'].replace([1,2,3,5],0, inplace=True)
        p['never_married'].replace(4,1, inplace=True)
        p['unmarried_couple'] = p['MARITAL']
        p['unmarried_couple'].replace([1,2,3,4],0, inplace=True)
        p['unmarried_couple'].replace(5,1, inplace=True)
        p = p.drop(['MARITAL'], axis=1)

        #RENTHOM1
        p['own_house'] = p['RENTHOM1']
        p['own_house'].replace([1,2],2, inplace=True)
        p['own_house'].replace(0,1, inplace=True)
        p['own_house'].replace(2,0, inplace=True)
        p['renting'] = p['RENTHOM1']
        p['renting'].replace([0,2],0, inplace=True)
        p['other_arrangement_housing'] = p['RENTHOM1']
        p['other_arrangement_housing'].replace([0,1],0, inplace=True)
        p['other_arrangement_housing'].replace(2,1, inplace=True)
        p = p.drop(['RENTHOM1'], axis=1)

        #EMPLOY1
        p['employed_for_wages'] = p['EMPLOY1']
        p['employed_for_wages'].replace(0,10, inplace=True)
        p['employed_for_wages'].replace([1,2,3,4,5,6,7],0, inplace=True)
        p['employed_for_wages'].replace(10,1, inplace=True)
        p['self_employed'] = p['EMPLOY1']
        p['self_employed'].replace([2,3,4,5,6,7],0, inplace=True)
        p['out_of_work_year_plus'] = p['EMPLOY1']
        p['out_of_work_year_plus'].replace([1,3,4,5,6,7],0, inplace=True)
        p['out_of_work_year_plus'].replace(2,1, inplace=True)
        p['out_of_work_year_less'] = p['EMPLOY1']
        p['out_of_work_year_less'].replace([1,2,4,5,6,7],0, inplace=True)
        p['out_of_work_year_less'].replace(3,1, inplace=True)
        p['homemaker'] = p['EMPLOY1']
        p['homemaker'].replace([1,2,3,5,6,7],0, inplace=True)
        p['homemaker'].replace(4,1, inplace=True)
        p['student'] = p['EMPLOY1']
        p['student'].replace([1,2,3,4,6,7],0, inplace=True)
        p['student'].replace(5,1, inplace=True)
        p['retired'] = p['EMPLOY1']
        p['retired'].replace([1,2,3,4,5,7],0, inplace=True)
        p['retired'].replace(6,1, inplace=True)
        p['unable_to_work'] = p['EMPLOY1']
        p['unable_to_work'].replace([1,2,3,4,5,6],0, inplace=True)
        p['unable_to_work'].replace(7,1, inplace=True)
        p = p.drop(['EMPLOY1'], axis=1)

        #SMOKDAY2
        p['smoke_every_day'] = p['SMOKDAY2']
        p['smoke_every_day'].replace(0,3,inplace=True)
        p['smoke_every_day'].replace([1,2],0,inplace=True)
        p['smoke_every_day'].replace(3,1,inplace=True)
        p['smoke_some_days'] = p['SMOKDAY2']
        p['smoke_some_days'].replace(2,0,inplace=True)
        p['smoke_not_at_all'] = p['SMOKDAY2']
        p['smoke_not_at_all'].replace(1,0,inplace=True)
        p['smoke_not_at_all'].replace(2,1,inplace=True)
        p = p.drop(['SMOKDAY2'], axis=1)

        #USENOW3
        p['smokeless_every_day'] = p['USENOW3']
        p['smokeless_every_day'].replace(0,3,inplace=True)
        p['smokeless_every_day'].replace([1,2],0,inplace=True)
        p['smokeless_every_day'].replace(3,1,inplace=True)
        p['smokeless_some_days'] = p['USENOW3']
        p['smokeless_some_days'].replace(2,0,inplace=True)
        p['smokeless_not_at_all'] = p['USENOW3']
        p['smokeless_not_at_all'].replace(1,0,inplace=True)
        p['smokeless_not_at_all'].replace(2,1,inplace=True)
        p = p.drop(['USENOW3'], axis=1)

        # ECIGNOW1
        p['ecig_every_day'] = p['ECIGNOW1']
        p['ecig_every_day'].replace(0,4,inplace=True)
        p['ecig_every_day'].replace([1,2,3],0,inplace=True)
        p['ecig_every_day'].replace(4,1,inplace=True)
        p['ecig_some_days'] = p['ECIGNOW1']
        p['ecig_some_days'].replace([2,3],0,inplace=True)
        p['ecig_not_at_all'] = p['ECIGNOW1']
        p['ecig_not_at_all'].replace([1,3],0,inplace=True)
        p['ecig_not_at_all'].replace(2,1,inplace=True)
        p['ecig_never_used'] = p['ECIGNOW1']
        p['ecig_never_used'].replace([1,2],0,inplace=True)
        p['ecig_never_used'].replace(3,1,inplace=True)
        p = p.drop(['ECIGNOW1'], axis=1)

        #_IMPRACE
        p['white'] = p['_IMPRACE']
        p['white'].replace(0,6, inplace=True)
        p['white'].replace([1,2,3,4,5],0, inplace=True)
        p['white'].replace(6,1, inplace=True)
        p['black'] = p['_IMPRACE']
        p['black'].replace([2,3,4,5],0, inplace=True)
        p['asian'] = p['_IMPRACE']
        p['asian'].replace([1,3,4,5],0, inplace=True)
        p['asian'].replace(2,1, inplace=True)
        p['native'] = p['_IMPRACE']
        p['native'].replace([1,2,4,5],0, inplace=True)
        p['native'].replace(3,1, inplace=True)
        p['hispanic'] = p['_IMPRACE']
        p['hispanic'].replace([1,2,3,5],0, inplace=True)
        p['hispanic'].replace(4,1, inplace=True)
        p = p.drop(['_IMPRACE'], axis=1)

        #_EDUCAG
        p['not_graduate_high_school'] = p['_EDUCAG']
        p['not_graduate_high_school'].replace(0,4, inplace=True)
        p['not_graduate_high_school'].replace([1,2,3],0, inplace=True)
        p['not_graduate_high_school'].replace(4,1, inplace=True)
        p['graduated_high_school'] = p['_EDUCAG']
        p['graduated_high_school'].replace([2,3],0, inplace=True)
        p['attended_college'] = p['_EDUCAG']
        p['attended_college'].replace([1,3],0, inplace=True)
        p['attended_college'].replace(2,1, inplace=True)
        p['graduated_college'] = p['_EDUCAG']
        p['graduated_college'].replace([1,2],0, inplace=True)
        p['graduated_college'].replace(3,1, inplace=True)
        p = p.drop(['_EDUCAG'], axis=1)

        #FTJUDA2_
        p.loc[p['FTJUDA2_2'] == 1, 'FTJUDA2_'] /= 7
        p.loc[p['FTJUDA2_2'] == 2, 'FTJUDA2_'] /= 30
        p.loc[p['FTJUDA2_2'] == 3, 'FTJUDA2_'] /= 365
        p = p.drop(['FTJUDA2_2'], axis=1)

        #FRUTDA2_
        p.loc[p['FRUTDA2_2'] == 1, 'FRUTDA2_'] /= 7
        p.loc[p['FRUTDA2_2'] == 2, 'FRUTDA2_'] /= 30
        p.loc[p['FRUTDA2_2'] == 3, 'FRUTDA2_'] /= 365
        p = p.drop(['FRUTDA2_2'], axis=1)

        #GRENDA1_
        p.loc[p['GRENDA1_2'] == 1, 'GRENDA1_'] /= 7
        p.loc[p['GRENDA1_2'] == 2, 'GRENDA1_'] /= 30
        p.loc[p['GRENDA1_2'] == 3, 'GRENDA1_'] /= 365
        p = p.drop(['GRENDA1_2'], axis=1)

        #FRNCHDA_
        p.loc[p['FRNCHDA_2'] == 1, 'FRNCHDA_'] /= 7
        p.loc[p['FRNCHDA_2'] == 2, 'FRNCHDA_'] /= 30
        p.loc[p['FRNCHDA_2'] == 3, 'FRNCHDA_'] /= 365
        p = p.drop(['FRNCHDA_2'], axis=1)

        #POTADA1_
        p.loc[p['POTADA1_2'] == 1, 'POTADA1_'] /= 7
        p.loc[p['POTADA1_2'] == 2, 'POTADA1_'] /= 30
        p.loc[p['POTADA1_2'] == 3, 'POTADA1_'] /= 365
        p = p.drop(['POTADA1_2'], axis=1)

        #VEGEDA2_
        p.loc[p['VEGEDA2_2'] == 1, 'VEGEDA2_'] /= 7
        p.loc[p['VEGEDA2_2'] == 2, 'VEGEDA2_'] /= 30
        p.loc[p['VEGEDA2_2'] == 3, 'VEGEDA2_'] /= 365
        p = p.drop(['VEGEDA2_2'], axis=1)

        was_missing_columns=['PHYSHLTH_was_missing',
        'MENTHLTH_was_missing',
        'POORHLTH_was_missing',
        'PERSDOC3_was_missing',
        'MEDCOST1_was_missing',
        'CHECKUP1_was_missing',
        'EXERANY2_was_missing',
        'BPMEDS_was_missing',
        'TOLDHI3_was_missing',
        'CHOLMED3_was_missing',
        'CVDINFR4_was_missing',
        'CVDCRHD4_was_missing',
        'CVDSTRK3_was_missing',
        'ASTHMA3_was_missing',
        'ASTHNOW_was_missing',
        'CHCSCNCR_was_missing',
        'CHCOCNCR_was_missing',
        'CHCCOPD3_was_missing',
        'ADDEPEV3_was_missing',
        'CHCKDNY2_was_missing',
        'DIABETE4_was_missing',
        'HAVARTH5_was_missing',
        'VETERAN3_was_missing',
        'PREGNANT_was_missing',
        'DEAF_was_missing',
        'BLIND_was_missing',
        'DECIDE_was_missing',
        'DIFFWALK_was_missing',
        'DIFFDRES_was_missing',
        'DIFFALON_was_missing',
        'SMOKE100_was_missing',
        'ALCDAY5_was_missing',
        'AVEDRNK3_was_missing',
        'DRNK3GE5_was_missing',
        'MAXDRNKS_was_missing',
        'FLUSHOT7_was_missing',
        'PNEUVAC4_was_missing',
        'HIVTST7_was_missing',
        '_HLTHPLN_was_missing',
        'HTIN4_was_missing',
        'WTKG3_was_missing',
        '_INCOMG1_was_missing',
        'FTJUDA2__was_missing',
        'FRUTDA2__was_missing',
        'cholesterol_checked_within_year_was_missing',
        '_METSTAT_and_URBSTAT_was_missing',
        'BPHIGH6_was_missing',
        'MARITAL_was_missing',
        'RENTHOM1_was_missing',
        'EMPLOY1_was_missing',
        'SMOKDAY2_was_missing',
        'USENOW3_was_missing',
        'ECIGNOW1_was_missing',
        '_EDUCAG_was_missing']
        #was_missing_df = pd.DataFrame(0, index=np.arange(len(data)), columns=was_missing_columns)
        was_missing_df = pd.DataFrame(0, index=[0],columns=was_missing_columns)
        final=pd.concat([p,was_missing_df], axis=1)
        final = final.round(2)
        #final.to_csv('./input_final.csv')
        print(final.to_numpy())
        if heartml.predict(final)[0] == 1:
            return render_template('heart1.html')
        else:
            return render_template('heart0.html')
        #return str(heartml.predict(final)[0])
        #'''
        #    <h1>The SEXVAR value is: {}</h1>
        #    <h1>The GENHLTH value is: {}</h1>
        #    <h1>The PHYSHLTH value is: {}</h1>
        #    <h1>The MENTHLTH value is: {}</h1>'''.format(SEXVAR, GENHLTH, PHYSHLTH, MENTHLTH)

    # otherwise handle the GET request
    return send_from_directory('templates', path='heart.html')

#app.run(port=5000)

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
        p = p.astype(float)
        #p.to_csv('./input_test.csv')
        #framework = request.form.get('framework')
        #return "prediction {}.".format(automl.predict(p))

        #begin conversion to trained dataframe
        # BPHIGH6
        p['high_blood_pressure'] = p['BPHIGH6']
        p['high_blood_pressure'].replace([0,1,2],0, inplace=True)
        p['high_blood_pressure'].replace(3,1, inplace=True)
        p['pregnant_high_blood_pressure'] = p['BPHIGH6']
        p['pregnant_high_blood_pressure'].replace([0,1,3],0, inplace=True)
        p['pregnant_high_blood_pressure'].replace(2,1, inplace=True)
        p['borderline_high_blood_pressure'] = p['BPHIGH6']
        p['borderline_high_blood_pressure'].replace([0,2,3],0, inplace=True)
        p = p.drop(['BPHIGH6'], axis=1)

        #CHOLCHK3
        p['cholesterol_checked_within_year'] = p['CHOLCHK3']
        p = p.drop(['CHOLCHK3'], axis=1)

        #MARITAL
        p['married'] = p['MARITAL']
        p['married'].replace([1,2,3,4,5],2, inplace=True)
        p['married'].replace(0,1, inplace=True)
        p['married'].replace(2,0, inplace=True)
        p['divorced'] = p['MARITAL']
        p['divorced'].replace([0,2,3,4,5],0, inplace=True)
        p['widowed'] = p['MARITAL']
        p['widowed'].replace([1,3,4,5],0, inplace=True)
        p['widowed'].replace(2,1, inplace=True)
        p['separated'] = p['MARITAL']
        p['separated'].replace([1,2,4,5],0, inplace=True)
        p['separated'].replace(3,1, inplace=True)
        p['never_married'] = p['MARITAL']
        p['never_married'].replace([1,2,3,5],0, inplace=True)
        p['never_married'].replace(4,1, inplace=True)
        p['unmarried_couple'] = p['MARITAL']
        p['unmarried_couple'].replace([1,2,3,4],0, inplace=True)
        p['unmarried_couple'].replace(5,1, inplace=True)
        p = p.drop(['MARITAL'], axis=1)

        #RENTHOM1
        p['own_house'] = p['RENTHOM1']
        p['own_house'].replace([1,2],2, inplace=True)
        p['own_house'].replace(0,1, inplace=True)
        p['own_house'].replace(2,0, inplace=True)
        p['renting'] = p['RENTHOM1']
        p['renting'].replace([0,2],0, inplace=True)
        p['other_arrangement_housing'] = p['RENTHOM1']
        p['other_arrangement_housing'].replace([0,1],0, inplace=True)
        p['other_arrangement_housing'].replace(2,1, inplace=True)
        p = p.drop(['RENTHOM1'], axis=1)

        #EMPLOY1
        p['employed_for_wages'] = p['EMPLOY1']
        p['employed_for_wages'].replace(0,10, inplace=True)
        p['employed_for_wages'].replace([1,2,3,4,5,6,7],0, inplace=True)
        p['employed_for_wages'].replace(10,1, inplace=True)
        p['self_employed'] = p['EMPLOY1']
        p['self_employed'].replace([2,3,4,5,6,7],0, inplace=True)
        p['out_of_work_year_plus'] = p['EMPLOY1']
        p['out_of_work_year_plus'].replace([1,3,4,5,6,7],0, inplace=True)
        p['out_of_work_year_plus'].replace(2,1, inplace=True)
        p['out_of_work_year_less'] = p['EMPLOY1']
        p['out_of_work_year_less'].replace([1,2,4,5,6,7],0, inplace=True)
        p['out_of_work_year_less'].replace(3,1, inplace=True)
        p['homemaker'] = p['EMPLOY1']
        p['homemaker'].replace([1,2,3,5,6,7],0, inplace=True)
        p['homemaker'].replace(4,1, inplace=True)
        p['student'] = p['EMPLOY1']
        p['student'].replace([1,2,3,4,6,7],0, inplace=True)
        p['student'].replace(5,1, inplace=True)
        p['retired'] = p['EMPLOY1']
        p['retired'].replace([1,2,3,4,5,7],0, inplace=True)
        p['retired'].replace(6,1, inplace=True)
        p['unable_to_work'] = p['EMPLOY1']
        p['unable_to_work'].replace([1,2,3,4,5,6],0, inplace=True)
        p['unable_to_work'].replace(7,1, inplace=True)
        p = p.drop(['EMPLOY1'], axis=1)

        #SMOKDAY2
        p['smoke_every_day'] = p['SMOKDAY2']
        p['smoke_every_day'].replace(0,3,inplace=True)
        p['smoke_every_day'].replace([1,2],0,inplace=True)
        p['smoke_every_day'].replace(3,1,inplace=True)
        p['smoke_some_days'] = p['SMOKDAY2']
        p['smoke_some_days'].replace(2,0,inplace=True)
        p['smoke_not_at_all'] = p['SMOKDAY2']
        p['smoke_not_at_all'].replace(1,0,inplace=True)
        p['smoke_not_at_all'].replace(2,1,inplace=True)
        p = p.drop(['SMOKDAY2'], axis=1)

        #USENOW3
        p['smokeless_every_day'] = p['USENOW3']
        p['smokeless_every_day'].replace(0,3,inplace=True)
        p['smokeless_every_day'].replace([1,2],0,inplace=True)
        p['smokeless_every_day'].replace(3,1,inplace=True)
        p['smokeless_some_days'] = p['USENOW3']
        p['smokeless_some_days'].replace(2,0,inplace=True)
        p['smokeless_not_at_all'] = p['USENOW3']
        p['smokeless_not_at_all'].replace(1,0,inplace=True)
        p['smokeless_not_at_all'].replace(2,1,inplace=True)
        p = p.drop(['USENOW3'], axis=1)

        # ECIGNOW1
        p['ecig_every_day'] = p['ECIGNOW1']
        p['ecig_every_day'].replace(0,4,inplace=True)
        p['ecig_every_day'].replace([1,2,3],0,inplace=True)
        p['ecig_every_day'].replace(4,1,inplace=True)
        p['ecig_some_days'] = p['ECIGNOW1']
        p['ecig_some_days'].replace([2,3],0,inplace=True)
        p['ecig_not_at_all'] = p['ECIGNOW1']
        p['ecig_not_at_all'].replace([1,3],0,inplace=True)
        p['ecig_not_at_all'].replace(2,1,inplace=True)
        p['ecig_never_used'] = p['ECIGNOW1']
        p['ecig_never_used'].replace([1,2],0,inplace=True)
        p['ecig_never_used'].replace(3,1,inplace=True)
        p = p.drop(['ECIGNOW1'], axis=1)

        #_IMPRACE
        p['white'] = p['_IMPRACE']
        p['white'].replace(0,6, inplace=True)
        p['white'].replace([1,2,3,4,5],0, inplace=True)
        p['white'].replace(6,1, inplace=True)
        p['black'] = p['_IMPRACE']
        p['black'].replace([2,3,4,5],0, inplace=True)
        p['asian'] = p['_IMPRACE']
        p['asian'].replace([1,3,4,5],0, inplace=True)
        p['asian'].replace(2,1, inplace=True)
        p['native'] = p['_IMPRACE']
        p['native'].replace([1,2,4,5],0, inplace=True)
        p['native'].replace(3,1, inplace=True)
        p['hispanic'] = p['_IMPRACE']
        p['hispanic'].replace([1,2,3,5],0, inplace=True)
        p['hispanic'].replace(4,1, inplace=True)
        p = p.drop(['_IMPRACE'], axis=1)

        #_EDUCAG
        p['not_graduate_high_school'] = p['_EDUCAG']
        p['not_graduate_high_school'].replace(0,4, inplace=True)
        p['not_graduate_high_school'].replace([1,2,3],0, inplace=True)
        p['not_graduate_high_school'].replace(4,1, inplace=True)
        p['graduated_high_school'] = p['_EDUCAG']
        p['graduated_high_school'].replace([2,3],0, inplace=True)
        p['attended_college'] = p['_EDUCAG']
        p['attended_college'].replace([1,3],0, inplace=True)
        p['attended_college'].replace(2,1, inplace=True)
        p['graduated_college'] = p['_EDUCAG']
        p['graduated_college'].replace([1,2],0, inplace=True)
        p['graduated_college'].replace(3,1, inplace=True)
        p = p.drop(['_EDUCAG'], axis=1)

        #FTJUDA2_
        p.loc[p['FTJUDA2_2'] == 1, 'FTJUDA2_'] /= 7
        p.loc[p['FTJUDA2_2'] == 2, 'FTJUDA2_'] /= 30
        p.loc[p['FTJUDA2_2'] == 3, 'FTJUDA2_'] /= 365
        p = p.drop(['FTJUDA2_2'], axis=1)

        #FRUTDA2_
        p.loc[p['FRUTDA2_2'] == 1, 'FRUTDA2_'] /= 7
        p.loc[p['FRUTDA2_2'] == 2, 'FRUTDA2_'] /= 30
        p.loc[p['FRUTDA2_2'] == 3, 'FRUTDA2_'] /= 365
        p = p.drop(['FRUTDA2_2'], axis=1)

        #GRENDA1_
        p.loc[p['GRENDA1_2'] == 1, 'GRENDA1_'] /= 7
        p.loc[p['GRENDA1_2'] == 2, 'GRENDA1_'] /= 30
        p.loc[p['GRENDA1_2'] == 3, 'GRENDA1_'] /= 365
        p = p.drop(['GRENDA1_2'], axis=1)

        #FRNCHDA_
        p.loc[p['FRNCHDA_2'] == 1, 'FRNCHDA_'] /= 7
        p.loc[p['FRNCHDA_2'] == 2, 'FRNCHDA_'] /= 30
        p.loc[p['FRNCHDA_2'] == 3, 'FRNCHDA_'] /= 365
        p = p.drop(['FRNCHDA_2'], axis=1)

        #POTADA1_
        p.loc[p['POTADA1_2'] == 1, 'POTADA1_'] /= 7
        p.loc[p['POTADA1_2'] == 2, 'POTADA1_'] /= 30
        p.loc[p['POTADA1_2'] == 3, 'POTADA1_'] /= 365
        p = p.drop(['POTADA1_2'], axis=1)

        #VEGEDA2_
        p.loc[p['VEGEDA2_2'] == 1, 'VEGEDA2_'] /= 7
        p.loc[p['VEGEDA2_2'] == 2, 'VEGEDA2_'] /= 30
        p.loc[p['VEGEDA2_2'] == 3, 'VEGEDA2_'] /= 365
        p = p.drop(['VEGEDA2_2'], axis=1)

        was_missing_columns=['PHYSHLTH_was_missing',
        'MENTHLTH_was_missing',
        'POORHLTH_was_missing',
        'PERSDOC3_was_missing',
        'MEDCOST1_was_missing',
        'CHECKUP1_was_missing',
        'EXERANY2_was_missing',
        'BPMEDS_was_missing',
        'TOLDHI3_was_missing',
        'CHOLMED3_was_missing',
        'CVDINFR4_was_missing',
        'CVDCRHD4_was_missing',
        'CVDSTRK3_was_missing',
        'ASTHMA3_was_missing',
        'ASTHNOW_was_missing',
        'CHCSCNCR_was_missing',
        'CHCOCNCR_was_missing',
        'CHCCOPD3_was_missing',
        'ADDEPEV3_was_missing',
        'CHCKDNY2_was_missing',
        'DIABETE4_was_missing',
        'HAVARTH5_was_missing',
        'VETERAN3_was_missing',
        'PREGNANT_was_missing',
        'DEAF_was_missing',
        'BLIND_was_missing',
        'DECIDE_was_missing',
        'DIFFWALK_was_missing',
        'DIFFDRES_was_missing',
        'DIFFALON_was_missing',
        'SMOKE100_was_missing',
        'ALCDAY5_was_missing',
        'AVEDRNK3_was_missing',
        'DRNK3GE5_was_missing',
        'MAXDRNKS_was_missing',
        'FLUSHOT7_was_missing',
        'PNEUVAC4_was_missing',
        'HIVTST7_was_missing',
        '_HLTHPLN_was_missing',
        'HTIN4_was_missing',
        'WTKG3_was_missing',
        '_INCOMG1_was_missing',
        'FTJUDA2__was_missing',
        'FRUTDA2__was_missing',
        'cholesterol_checked_within_year_was_missing',
        '_METSTAT_and_URBSTAT_was_missing',
        'BPHIGH6_was_missing',
        'MARITAL_was_missing',
        'RENTHOM1_was_missing',
        'EMPLOY1_was_missing',
        'SMOKDAY2_was_missing',
        'USENOW3_was_missing',
        'ECIGNOW1_was_missing',
        '_EDUCAG_was_missing']
        #was_missing_df = pd.DataFrame(0, index=np.arange(len(data)), columns=was_missing_columns)
        was_missing_df = pd.DataFrame(0, index=[0],columns=was_missing_columns)
        final=pd.concat([p,was_missing_df], axis=1)
        final = final.round(2)
        #final.to_csv('./input_final.csv')
        print(final.to_numpy())
        if automl.predict(final)[0] == 1:
            return render_template('process1.html')
        else:
            return render_template('process0.html')
        #return str(automl.predict(final)[0])
        #'''
        #    <h1>The SEXVAR value is: {}</h1>
        #    <h1>The GENHLTH value is: {}</h1>
        #    <h1>The PHYSHLTH value is: {}</h1>
        #    <h1>The MENTHLTH value is: {}</h1>'''.format(SEXVAR, GENHLTH, PHYSHLTH, MENTHLTH)

    # otherwise handle the GET request
    return send_from_directory('templates', path='diabetes.html')

if __name__ == '__main__':
    app.run()
