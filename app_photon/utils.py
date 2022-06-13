import os , shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

from config import Config
from app_photon.search_config import SearchConfig


# функция обращения к фотон
def photon_parsing() -> None:
    os.system(
        f'python Photon\photon.py --url {SearchConfig.URL} '
        f'--export=json '
        f'--output "{Config.OS_PATH_RESULT}" '
        f'{SearchConfig.PARAMETERS_SEARCH}')


# функция архивации директории shutil
def zip_result() -> None:
    zip_path = shutil.make_archive(root_dir=Config.OS_PATH_RESULT, base_name='zipped_scrap', format='zip')
    SearchConfig.ZIP_PATH = zip_path

def change_directory_zipped():
    os.replace(SearchConfig.ZIP_PATH, Config.OS_PATH_RESULT)


# функция чистящая параметры и рещультаты поиска
def cleaner() -> None:
    shutil.rmtree(Config.OS_PATH_RESULT)
    SearchConfig.URL = ''
    SearchConfig.PARAMETERS_SEARCH = ' '


# конфигурирует параметры поиска
def set_search_param(form):
    SearchConfig.URL = form.url.data
    if form.clone.data is True:
        SearchConfig.PARAMETERS_SEARCH += '--clone '
    if form.only_urls.data is True:
        SearchConfig.PARAMETERS_SEARCH += '--only-urls '
    if form.keys.data is True:
        SearchConfig.PARAMETERS_SEARCH += '--keys '
    if form.dns.data is True:
        SearchConfig.PARAMETERS_SEARCH += '--dns '

# создает и сохраняет цсв файл
def data_csv():
    X = np.zeros((150, 2))
    np.random.seed(seed=42)
    X[:50, 0] = np.random.normal(loc=0.0, scale=.3, size=50)
    X[:50, 1] = np.random.normal(loc=0.0, scale=.3, size=50)
    X[50:100, 0] = np.random.normal(loc=2.0, scale=.5, size=50)
    X[50:100, 1] = np.random.normal(loc=-1.0, scale=.2, size=50)
    X[100:150, 0] = np.random.normal(loc=-1.0, scale=.2, size=50)
    X[100:150, 1] = np.random.normal(loc=2.0, scale=.5, size=50)
    frame = pd.DataFrame(X)
    frame.to_csv('eggs.csv', index=False, )


def csv_reader(path_to_csv: str) -> list:
    data_klaster = []
    result = []
    with open(path_to_csv) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data_klaster.append(row)
    for data in data_klaster:
        row_data = []
        for i in data:
            row_data.append(float(i))
        result.append(row_data)
    return result

