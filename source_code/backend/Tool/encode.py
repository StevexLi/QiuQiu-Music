import chardet
import requests


def get_code(file_url):
    file = requests.get(file_url)
    return chardet.detect(file.content)['encoding']
