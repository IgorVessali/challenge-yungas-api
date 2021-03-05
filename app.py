from flask import Flask, request
from database import formated_data
from regions import list_regions
from utils import paginate

peoples_db = formated_data()
lst_regions = list_regions()

app = Flask(__name__) 

# Creates the end-poit that returns the index to API
@app.route('/')
def index():
  return '<h1> Code Challenger Yungas</h1> <br> <h3>by: Igor Vessali </h3>'

# Creates the end-point that returns a list of all people
# 'page_size'-'optional'-> number of items on the page
# 'page'-'optional'-> current page
@app.route('/peoples', methods=['GET'])
def get_peoples(page_size = 20, page = 1):
  if request.args.get('page_size'): page_size = int(request.args.get('page_size'))   
  if request.args.get('page'): page = int(request.args.get('page')) 

  return paginate(peoples_db, page_size, page), 200

# Creates the end-point that returns a list of people by region based on the state reported
# 'page_size'-'optional'-> number of items on the page
# 'page'-'optional'-> current page
@app.route('/peoples/<region>', methods=['GET'])
def get_peoples_per_region(region, page_size = 20, page = 1):  
  if request.args.get('region'): 
    return {"err": "The 'region' field is mandatory"}
  if request.args.get('page_size'): page_size = int(request.args.get('page_size'))
  if request.args.get('page'): page = int(request.args.get('page')) 

  ret_peoples = [ people for people in peoples_db if people['location']['region'] == region ]
  return paginate(ret_peoples, page_size, page), 200
  
# Creates the end-point that returns a list of regions
# 'page_size'-'optional'-> number of items on the page
# 'page'-'optional'-> current page
@app.route('/regions', methods=['GET'])
def get_regions(page_size = 20, page = 1):
  if request.args.get('page_size'): page_size = int(request.args.get('page_size'))   
  if request.args.get('page'): page = int(request.args.get('page')) 

  return paginate(lst_regions, page_size, page), 200

if __name__ == '__main__':
  app.run(debug=True)


    