from flask import Flask, request, jsonify

app = Flask(__name__)

# Seed value
seed_value = 0

@app.route('/', methods=['GET'])
def get_seed():
    global seed_value
    # Return the seed value as a string
    return str(seed_value)

@app.route('/', methods=['POST'])
def update_seed():
    global seed_value
    data = request.get_json()
    # Update the seed value if 'num' is in the JSON body
    if 'num' in data:
        try:
            # Check if the provided number is an integer
            num = int(data['num'])
            seed_value = num
            return jsonify(success=True), 200
        except ValueError:
            # If 'num' is not an integer, return an error
            return jsonify(error="The provided value is not an integer."), 400
    else:
        # If 'num' is not provided, return an error
        return jsonify(error="Missing 'num' in the request body."), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)