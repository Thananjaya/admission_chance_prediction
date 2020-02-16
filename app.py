import pickle
import numpy as np
from flask import Flask, render_template
from forms import AdmissionPredictionForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '34ff6a9706c5e3da28cafae2cf5ae03b'

@app.route('/', methods=['GET', 'POST'])
def home():
    form = AdmissionPredictionForm()
    print(form.validate())
    if form.validate_on_submit():
        features = [int(i) if isinstance(i, str) else i for i in list(form.data.values())[:-2]]
        to_predict = np.array(features).reshape(1,-1)
        loaded_model = pickle.load(open("model/model.pkl","rb"))
        result = loaded_model.predict(to_predict)
        return render_template('home.html', form=form, result=int(result[0]*100))
    else:
        return render_template('home.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)