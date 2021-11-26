import numpy as np
from flask import Flask, request, render_template
from keras.models import load_model 

flask_app = Flask(__name__)
model = load_model('AHPTtrainedNNmodel.h5')

mapping_features = {
    "Yes": 1,"No": 0,"lncfm": 0,"bncfm": 0.5,"mncfm": 1,
    "npa": 0,"spa": 1/3,"gpa": 2/3,"mpa": 1,"nds": 0,
    "sds": 1/3,"gds": 2/3,"mds": 1,"nalc": 0,"salc": 1/3,
    "falc": 2/3,"aalc": 1,"Automobile": 0,"Motorbike": 1/4,
    "pub": 1/2,"Bike": 3/4,"Walking": 1
}
mapping_labels = {
    "0": "Insufficient_Weight",
    "1": "Normal_Weight",
    "2": "Overweight_Level_I",
    "3": "Overweight_Level_II",
    "4": "Overweight_Level_III",
    "5": "Obesity_Type_I",
    "6": "Obesity_Type_II",
    "7": "Obesity_Type_III"
}

@flask_app.route("/")
def Home():
    return render_template("index.html")


@flask_app.route("/predict", methods = ["POST"])
def predict():
    features = []
    for i, value in enumerate(request.form.values()):
        if value in mapping_features:
            features.append(mapping_features[value])
        else:
            if i == 12: features.append((float(value)-14)/47)
            else: features.append((float(value)-1)/3)
    features = np.array([features], dtype=np.float)
    prediction = str(np.argmax(model.predict(features)))
    
    out = {}
    if request.form['Gender'] == 'No':
        out['Gender?'] = "Female" 
    else:
        out['Gender?']="Male"
    out['History of Obesity in Family?'] = request.form['FHO']
    out['Frequently Consume High Caloric Food?'] = request.form['FAVC']
    out['Frequently Consume Vegetables?'] = request.form['FCVC']
    if request.form['CAEC'] == 'nalc':
        out['Eat Between Meals Often?'] = "Never"
    elif request.form['CAEC'] == 'salc':
        out['Eat Between Meals Often?'] = "Sometimes"
    elif request.form['CAEC'] == 'falc':
        out['Eat Between Meals Often?'] = "Freqently"
    else:
        out['Eat Between Meals Often?'] = "Always"
    out['Smoke?'] = request.form['SMOKE']
    if request.form['CH20'] == 'lncfm':
        out['Water Consumption?'] = "Less than a liter"
    elif request.form['CAEC'] == 'bncfm':
        out['Water Consumption?'] = "Between 1 and 2 L"
    else:
        out['Water Consumption?'] = "More than 2 L"

    out['Monitor Daily Calories?'] = request.form['SCC']
    
    if request.form['FAF'] == 'npa':
        out['Freqency of Physical Activity?'] = "Never"
    elif request.form['CAEC'] == 'spa':
        out['Freqency of Physical Activity?'] = "1 or 2 days"
    elif request.form['CAEC'] == 'gpa':
        out['Freqency of Physical Activity?'] = "2 or 4 days"
    else:
        out['Freqency of Physical Activity?'] = "4 or 5 days"
    
    if request.form['TUE'] == 'nds':
        out['Time Spent on Devices Per Day?'] = "0-2 hours"
    elif request.form['CAEC'] == 'sds':
        out['Time Spent on Devices Per Day?'] = "3-5 hours"
    elif request.form['CAEC'] == 'gds':
        out['Time Spent on Devices Per Day?'] = "More than 5 hours"
    else:
        out['Time Spent on Devices Per Day?'] = "Always"

    if request.form['CALC'] == 'nalc':
        out['Alcohol Consumption?'] = "Never"
    elif request.form['CAEC'] == 'salc':
        out['Alcohol Consumption?'] = "Sometimes"
    elif request.form['CAEC'] == 'falc':
        out['Alcohol Consumption?'] = "Freqently"
    else:
        out['Alcohol Consumption?'] = "Always"

    if request.form['mtrans'] == 'pub':
        out['Primary Mode of Transportation?'] = "Public Transportation"
    else:
        out['Primary Mode of Transportation?'] = request.form['mtrans']

    out['Age'] = request.form['Age']
    out['Meal Per Day'] = request.form['NCP']

    return render_template("out.html", result = out,prediction_text = "The health classification is {}".format(mapping_labels[prediction]))

if __name__ == "__main__":
    flask_app.run(debug=True)