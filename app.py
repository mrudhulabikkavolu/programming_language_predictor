from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open("model.pkl","rb"))
vectorizer = pickle.load(open("vectorizer.pkl","rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    code = request.form['code']

    code_vector = vectorizer.transform([code])

    prediction = model.predict(code_vector)

    return render_template("index.html", prediction=prediction[0])


if __name__ == "__main__":
    app.run(debug=True)