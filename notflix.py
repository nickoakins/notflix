
import os
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

import sqlite3

###db="C:/Users/nicko/NotFlix/db/flix.db"


import configparser
config = configparser.ConfigParser()
config.read('NotFlix.conf')
db = config ['database']['file']

print ( db )

@app.route('/')
def index():
    conn = sqlite3.connect( db )
    c = conn.cursor()
    c.execute('SELECT * FROM flix')

    data = c.fetchall()

##or
##c.fetchmany(20)

    return render_template('index.html', data=data)

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello %s!</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)

