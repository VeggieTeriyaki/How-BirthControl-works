from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import random
import csv 
geneapp = Flask(__name__)
geneapp.config.from_object(__name__)
geneapp.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
@geneapp.route("/",methods=['GET', 'POST'])

def alleles():
    form = ReusableForm(request.form)
 
    print (form.errors)
    if request.method == 'POST':
        name=request.form['gene']
        print (name)
 
        if form.validate():
            # Save the comment here.
            flash('Hello ' + name +', your randomly generated gene and rs number is %s' %(getRandomRSAndGene(),))
        else:
            flash('All the form fields are required. ')
 
    return render_template('alleles.html', form=form)