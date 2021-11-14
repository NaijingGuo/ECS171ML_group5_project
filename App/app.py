import numpy as np
from flask import Flask, request, render_template
from keras.models import load_model 
# Create flask app
flask_app = Flask(__name__)
model = load_model('AHPTtrainedNNmodel.h5')

mapping_features = {
    "Yes": 1,"No": 0,"lncfm": 0,"bncfm": 0.5,"mncfm": 1,
    "npa": 0,"spa": 1/3,"gpa": 2/3,"mpa": 1,"nds": 0,
    "sds": 1/3,"gds": 2/3,"mds": 1,"nalc": 0,"salc": 1/3,
    "falc": 2/3,"aalc": 1,"Automobile": 0,"Motorbike": 1,
    "pub": 2,"Bike": 3,"Walking": 4
}
mapping_labels = {
    "0": "Insufficient_Weight",
    "1": "Normal_Weight",
    "2": "Overweight_Level_I",
    "3": "Overweight_Level_II",
    "4": "Overweight_Level_III"
}

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    features = []
    for value in request.form.values():
        if value in mapping_features:
            features.append(mapping_features[value])
        else:
            features.append(value)
    features = np.array([features], dtype=np.float)
    prediction = str(np.argmax(model.predict(features)))
    return render_template("index.html", prediction_text = "The health classification is {}".format(mapping_labels[prediction]))

if __name__ == "__main__":
    flask_app.run(debug=True)