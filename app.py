from flask import Flask, jsonify
from database import formated_data

peoples_db = formated_data()
app = Flask(__name__) 

# Creates the end-poit that returns the index to API
@app.route('/')
def index():
  return '<h1> Code Challenger Yungas</h1> <br> <h3>by: Igor Vessali </h3>'


# Creates the end-point that returns a list of all people
@app.route('/peoples', methods=['GET'])
def get_peoples(): 

  return jsonify(peoples_db), 200
  
  # Creates the end-point that returns a list of people by region based on the state reported
@app.route('/peoples/<region>', methods=['GET'])
def get_peoples_per_region(region):  
  if not region: 
    return {"err": "The 'region' parameter is mandatory"}

  ret_peoples = [ people for people in peoples_db if people['location']['region'] == region ]
  return jsonify(ret_peoples), 200

if __name__ == '__main__':
  app.run(debug=True)


    