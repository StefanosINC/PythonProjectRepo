from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
   # name = "Jose"
   # # you actually pass in my_variable
   # mylist = [1, 3, 4, 5, 6]
    #letters = list(name)
   # user_logged_in = True
   # pup_dictionary = {'pup_name': 'Sammy'}
    #return render_template('basic.html', user_logged_in= user_logged_in, name=name,letters=letters, pup_dictionary= pup_dictionary, mylist=mylist) #its going to look in the templates folder and same level 
    return render_template('home.html')
@app.route('/num')
def num():
    mylist = [1, 3, 4, 5, 6]
    return render_template('basic.html', mylist=mylist)
if __name__ == '__main__':
    app.run(debug=False)