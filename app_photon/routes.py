# -*- coding: utf-8 -*-
from flask import render_template, url_for, request, redirect, send_file, flash
from app_photon import app
from app_photon.search_config import SearchConfig
from app_photon.forms import Parsing, DataGenerator, Image
from app_photon.utils import data_csv, photon_parsing, cleaner, zip_result, set_search_param, csv_reader


@app.route('/', methods=['GET', 'POST'])
def index():
    form = Parsing()
    if request.method == 'POST':
        set_search_param(form)
        photon_parsing()
        zip_result()
        cleaner()
        flash('Good parsing, start sending file!')
        return redirect(url_for('download'))
    else:
        return render_template('index.html', form=form,
                               title='Photon',
                               description='Enter url choise arguments and press download zip')


@app.route('/download')
def download():
    # Отправляет файл(send file)
    return send_file(SearchConfig.ZIP_PATH, 'zipped_scrap')


@app.route('/data/generator', methods=['GET', 'POST'])
def data_generator():
    form = DataGenerator()
    if request.method == 'POST':
        data_csv()
        return redirect(url_for('download_csv'))
    return render_template('data_generator.html', form=form,
                           title='Data Generator',
                           description='Press download to get data for analyz')


@app.route('/download/CSV')
def download_csv():
    return send_file(SearchConfig.CSV_PATH, 'eggs')




@app.route('/claster', methods=['GET', 'POST'])
def claster():
    form = Image

    return render_template('render_data_image.html', form=form,
                           title='Claster Generator',
                           description='Upload csv file and press download to get image')