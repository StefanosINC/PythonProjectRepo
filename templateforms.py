from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup_form')
def signup_form():
    return render_template('signup.html')

@app.route('/thankyou')
def thank_you():
    first = request.args.get('first') ## This is how we will handle request data we get
    last = request.args.get('last')
    return render_template('thankyou.html', first=first, last=last)
def pup_name(name):
    return render_template('puppy.html', name=name)

@app.errorhandler(404) ## Error handling
def page_not_found(error):
    return render_template('404.html'), 404
if __name__ == '__main__':
    app.run(debug=True)