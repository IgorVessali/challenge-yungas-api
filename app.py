from flask import Flask

app = Flask(__name__) 

@app.route('/')
def index():
    return '<h1> Code Challenger Yungas</h1> <br> <h3>by: Igor Vessali </h3>'

if __name__ == '__main__':
  app.run(debug=True)


    