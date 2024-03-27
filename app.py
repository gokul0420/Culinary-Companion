from flask import Flask, render_template, request, jsonify
from gradio_client import Client

app = Flask(__name__)

client = Client("https://wizzseen-food.hf.space/")

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        ingredients = request.form['ingredients']
        result = client.predict(ingredients, api_name="/predict")
    return render_template('index.html', result=result)

@app.route('/get_result', methods=['POST'])
def get_result():
    ingredients = request.json['ingredients']
    result = client.predict(ingredients, api_name="/predict")
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
