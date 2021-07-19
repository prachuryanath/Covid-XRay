from flask import Flask, render_template, request
from scipy.misc import imsave, imread, imresize

app = Flask(__name__)

@app.route('/')
def index_view():
    return render_template('index.html')


@app.route('/predict',methods=['GET','POST'])
def predict():
	response = "COVID 19 Prediction"
return response	

if __name__ == '__main__':
    app.run(debug=True, port=8000)