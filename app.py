#===============================================================================================================================
#   File with functions to start the project and create the routes
#===============================================================================================================================
from flask import Flask, request, render_template, abort, jsonify
from database import formated_data
from regions import list_regions
from utils import paginate, verifyPaginateParam

peoples_db = formated_data()
lst_regions = list_regions()

app = Flask(__name__) 

# Creates the end-poit that returns the index to API
@app.route('/')
def index():
  return render_template('index.html') 


# Creates the end-point that returns a list of all people
# 'page_size'-'optional'-> number of items on the page
# 'page'-'optional'-> current page
@app.route('/peoples', methods=['GET'])
def get_peoples(page_size = 20, page = 1):  
  if verifyPaginateParam(page_size, page):
    return paginate(peoples_db, page_size, page), 200
  else: abort(404, description="OOOPS!")


# Creates the end-point that returns a list of people by region based on the state reported
# 'page_size'-'optional'-> number of items on the page
# 'page'-'optional'-> current page
@app.route('/peoples/<region>', methods=['GET'])
def get_peoples_per_region(region, page_size = 20, page = 1): 
  if region in lst_regions:
    if verifyPaginateParam(page_size, page):
      ret_peoples = [ people for people in peoples_db if people['location']['region'] == region ]
      return paginate(ret_peoples, page_size, page), 200
    else: abort(404, description="OOOPS!")
  else: return abort(404, description="The reported region does not exist, see a list in http://127.0.0.1:5000/regions")

  
# Creates the end-point that returns a list of regions
# 'page_size'-'optional'-> number of items on the page
# 'page'-'optional'-> current page
@app.route('/regions', methods=['GET'])
def get_regions(page_size = 20, page = 1):
  if verifyPaginateParam(page_size, page):
    return paginate(lst_regions, page_size, page), 200
  else: abort(404, description="OOOPS!")


# Define a 404 return
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404
  

if __name__ == '__main__':
  app.run(debug=True)


    