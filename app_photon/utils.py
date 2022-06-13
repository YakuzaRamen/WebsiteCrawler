import os
import shutil

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

# функция предположительно возвращает архив для отгрузки пользователю
