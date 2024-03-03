from flask import Flask, request
from flask_cors import CORS
from googletrans import Translator

app = Flask(__name__)
CORS(app)
PORT = 5001


@app.route('/')
def index():
    return "Welcome to AIMS verison 2.0"

@app.route('/dotranslate', methods=['GET', 'POST'])
def dotranslate():
    a = 'key'
    data = request.get_json()
    # print(data)
    language = data['b']
    objects = data['c']
    imageurl = data['d']
    print("lang : "+ language +" obj : "+objects+ " imgurl : "+imageurl)

    translator = Translator()
    trans = translator.translate(objects, dest=language)

    print(trans)
    # print(trans.text)
    return {imageurl : trans.text}



if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=PORT,
        debug=True,
        threaded=True
    )