from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Hello Puppy~! </h1>' #127.0.0.1:5000

@app.route('/information')
def info():
    return "<h1> Puppies are cute </h1>" #127.0.0.1:5000/information

# Dynamic Result
@app.route('/puppy/<name>')
def puppy(name):
    return f"<h1> This is a page for {name.upper()} </h1>" ## This works

@app.route('/puppy_latin/<name>')
def puppyLatin(name):
    print(name[-1])
    if name[-1] == 'y':
        print(name[-1])
        return f"<h1> YES!"
    else:
        name = name + "iful"
        return f"<h1> {name}"
if __name__ == '__main__':
    app.run()

# if name does not end in a y add a y
#if a name does in y replace it with iful