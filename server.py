from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__, template_folder='template', static_folder='static')

@app.route('/')
def home():
    return render_template('app.html')


@app.route('/classify_image', methods=['POST'])
def classify_image():
    image_data = request.form['image_data']
    response = jsonify(util.classify_image(image_data))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    
    # Load artifacts and model once before handling any requests
    util.load_saved_artifacts()
    util.load_model()
    
    app.run(port=5000)
