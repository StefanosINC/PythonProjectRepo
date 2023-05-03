from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, 
                     RadioField, SelectField, TextAreaField,  SubmitField)

from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

# Validate on submit is going to check the validators
class InfoForm(FlaskForm):
    breed = StringField('What breed are you?',validators=[DataRequired()]) #Requiring Data for input
    neutered = BooleanField("Have you been neutered?")
    mood = RadioField('Please Choose Your Mood:', 
                      choices=
                      [('mood_one', 'Happy'), 
                      ('mood_two', 'Excited')]) #List of tuple pairs
    food_choice = SelectField(u'Pick your favorite food:',
                              choices=
                              [('chi', 'Chicken'),
                               ('bf', 'Beef'),
                               ('fish', 'Fish')])
    feedback = TextAreaField()
    submit = SubmitField('Submit!')

@app.route('/', methods=['GET', 'POST'])
def index():
    # if the form is valid i grab that session and then I turn it to a redirect to thank
    form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data
        return redirect(url_for('thankyou')) # only happens when they submnit the form
    
    return render_template('index.html', form=form) #OG render

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)