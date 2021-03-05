from flask import Flask, jsonify
from database import database

peoples_db = database()
app = Flask(__name__) 

# Creates the end-poit that returns the index to API
@app.route('/')
def index():
  return '<h1> Code Challenger Yungas</h1> <br> <h3>by: Igor Vessali </h3>'


# Creates the end-point that returns a list of all people
@app.route('/peoples', methods=['GET'])
def get_peoples(): 

  return jsonify(peoples_db), 200

if __name__ == '__main__':
  app.run(debug=True)


    