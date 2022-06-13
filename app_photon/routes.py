# -*- coding: utf-8 -*-
from flask import render_template, url_for, request, redirect, send_file
from app_photon import app
from app_photon.search_config import SearchConfig
from app_photon.forms import Parsing
from app_photon.utils import photon_parsing, cleaner, zip_result, set_search_param


@app.route('/', methods=['GET', 'POST'])
def index():
    form = Parsing()
    if request.method == 'POST':
                set_search_param(form)
                photon_parsing()
                zip_result()
                cleaner()
                return redirect(url_for('download'))
    else:
        return render_template('index.html', form=form)


@app.route('/download')
def download():
    #Отправляет файл(send file)
    return send_file(SearchConfig.ZIP_PATH, 'zipped_scrap')
