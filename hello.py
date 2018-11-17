#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

@app.route('/')
def accueil():
    mots = ["bonjour", "à", "toi,", "visiteur."]
    return render_template('accueil.html', titre="Bienvenue !", mots=mots)

@app.route('/date')
def date():
    d = date.today().isoformat()
    return render_template('date.html', la_date=d)



if __name__ == '__main__':
    app.run(debug=True)





