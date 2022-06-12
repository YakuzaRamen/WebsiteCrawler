# -*- coding: utf-8 -*-
from flask import render_template
from app_photon import app
from app_photon.forms import Parsing


@app.route('/')
@app.route('/index')
def index():
    form = Parsing()
    return render_template('index.html', form=form)
