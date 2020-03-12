from flask import Flask, request, render_template

from quelfilm.engine import Classifier
from quelfilm.settings import *


app = Flask(__name__, template_folder=TEMPLATES_DIR)
classifier = Classifier()


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/predict')
def predict():
    text = request.args.get('text', '')
    intent, score, response_msg = classifier.predict(text)

    return {
        'intent': intent,
        'score': score,
        'response': response_msg
    }


def start():
    app.run(port=3000)


if __name__ == '__main__':
    start()
