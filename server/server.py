from flask import Flask, jsonify
from flask_cors import CORS

# app instance
app = Flask(__name__)
CORS(app)

# /api/home
@app.route("/api/home", methods=['GET'])
def return_home():
    return jsonify({
        'message': "Auth!",
        'people': ['User1', 'User2', 'User3']
    })


if __name__ == "__main__":
    # app.run(debug=True) # 5000
    app.run(debug=True, port=8080)
