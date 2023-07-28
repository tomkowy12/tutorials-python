import os
import zipfile
import requests

class FileFromWeb:
    def __init__(self, url: str, temp_file: str) -> None:
        self.url = url
        self.temp_file = temp_file

    def __enter__(self):
        try:
            response = requests.get(self.url)
        except Exception as e:
            print(e)
            raise e
        with open(self.temp_file, "wb") as f:
            f.write(response.content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exc_type={}".format(exc_type))
        print("exc_val={}".format(exc_val))
        print("exc_tb={}".format(exc_tb))
        if exc_type == FileNotFoundError:
            print("This error occured:\n\n", exc_val)
            return True
        elif exc_type == KeyError:
            print("This error occured:\n\n", exc_val)
            return True
        else:
            return False

ZIP_DIR = "/home/tomek/Projects/tutorials-python/Python/udemy_python_mid_advanced_mobilo/Section11-ContextManager/"
ZIP_NAME = ZIP_DIR + "euroxref.zip"
ZIP_URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip"
with FileFromWeb(ZIP_URL, ZIP_NAME) as f:
    with zipfile.ZipFile(f.temp_file, "r") as z:
        a_file = z.namelist()[0]
        print(a_file)
        os.chdir(ZIP_DIR)
        z.extract(a_file, ".", None)
