from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import random
import csv 
import geneapp
from flask import g
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    allele = TextField('Allele: ',validators=[validators.required()])
def getRandom():
    with open('genes.csv', newline='') as csvfile:
     genes = csv.reader(csvfile, delimiter=',')
     count = 0
     genie = ""
     rand = random.randint(2,200)
     for row in genes:
        if(row[0] != ''):
            genie = row[0]
        count +=1
        if (count == rand):
            return [row,genie]
random1 = getRandom()
Al =""
for allele in random1[0][2]:
    Al = Al + allele
for allele in random1[0][3].split(", "):
    Al = Al +" " + allele
message = 'Hello, your randomly generated gene is ' + random1[1] + ' and rs number is ' + random1[0][1] +'. The possible alleles that you can input here are: '+Al
@app.route("/")
def getRandomRSAndGene():
    global random1
    global message
    Al = ""

    form = ReusableForm(request.form)
    
    return render_template('hello.html', message = message,random1 = random1, form = form)

@app.route("/", methods=['GET', 'POST'])
def hello():
    global random1
    global message
    form = ReusableForm(request.form)
    print (form.errors)
    if request.method == 'POST':
        allele=request.form['allele']
        print (allele)
        if form.validate():
            # Save the comment here.
            if (allele == random1[0][2]):
                flash('The allele you chose is the expected allele. Hence, this birth control may just work on you!')
            elif(allele in random1[0][3].split(", ")):
                flash ('The allele you chose is a risk allele. Hence, this birth control may not work on you!')
            else:
                flash('Please enter a valid input!')
        else:
            flash('All the form fields are required. ')
            return render_template('hello.html', form=form, message = message)
    return render_template('hello.html', form=form, message = message)

if __name__ == "__main__":
    app.run()