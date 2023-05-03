from flask import Flask, render_template, request
from RequestHandler import RequestHandler
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('challenge.html')


@app.route('/challenge') 
def challenge(): ## Remember this has to equal the URL link
    username = request.args.get('username')  ## This is how we will handle request data we ge
    return RequestHandler.successfull_entry(username)
     

@app.errorhandler(404) ## Error handling
def page_not_found(error):
    return render_template('404.html'), 404



if __name__ == '__main__':
    app.run(debug=True)