import os
import zipfile
import requests
from contextlib import closing, suppress
 
 
class FileFromWeb:
 
    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file
 
    def download_file(self):
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self
 
    def close(self):
        # if os.path.isfile(self.tmp_file):
        os.remove(self.tmp_file)
 
import contextlib

ZIP_DIR = "/home/tomek/Projects/tutorials-python/Python/udemy_python_mid_advanced_mobilo/Section11-ContextManager/"
ZIP_NAME = ZIP_DIR + "euroxref.zip"
ZIP_URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip"
f = FileFromWeb(ZIP_URL, ZIP_NAME)
f.download_file()

with suppress(FileNotFoundError):
    with closing(FileFromWeb(ZIP_URL, ZIP_NAME)) as f:
        f.download_file()
        with zipfile.ZipFile(f.tmp_file, "r") as z:
            a_file = z.namelist()[0]
            print(a_file)
            os.chdir(ZIP_DIR)
            z.extract(a_file, ".", None)

            os.remove(f.tmp_file)

