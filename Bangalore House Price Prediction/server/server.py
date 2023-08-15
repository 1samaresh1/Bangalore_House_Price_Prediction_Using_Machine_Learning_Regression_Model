from flask import Flask, request, jsonify

from util import HousePricePredictor

app = Flask(__name__)
predictor = HousePricePredictor()


@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add("Access-Control-Allow-Headers",'*');
  

  
  return response

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    locations = predictor.get_location_names()
    
    return jsonify({'locations': locations})

@app.route('/predict_price', methods=['POST','GET'])
def predict_price():
    

    data = request.json
    location = data['location']
    sqft = data['sqft']
    bhk = data['bhk']
    bath = data['bath']

    estimated_price = predictor.get_estimated_price(location, sqft, bhk, bath)
    return jsonify({'estimated_price': estimated_price})

if __name__ == '__main__':
    app.run(debug=True)
