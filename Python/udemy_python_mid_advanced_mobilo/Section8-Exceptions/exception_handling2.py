import requests
import os
import shutil
 
def save_url_to_file(url, file_path):
        
    r = requests.get(url, stream = True)     
    with open(file_path, "wb") as f: 
        f.write(r.content)

def remove_if_exists(tmpfile_path):
    if os.path.isfile(tmpfile_path):
        print('Removing {}'.format(tmpfile_path))
        os.remove(tmpfile_path)
 
url = 'http://www.mobilo24.eu/spis/'
dir = 'udemy_python_mid_advanced_mobilo/Sections6&7-Classes_and_Extensions/temp'
tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

try:
    remove_if_exists(tmpfile_path)

    print('Downloading url {}'.format(url))
    save_url_to_file(url, tmpfile_path)

    print('Copying file {} {}'.format(tmpfile_path, file_path))
    shutil.copy(tmpfile_path, file_path)
except requests.exceptions.ConnectionError as e:
    print("Wrong address was provided. Details:\n{}".format(e))
except PermissionError as e:
    print("File {} can not be opened. Details: \n{}".format(tmpfile_path, e))
except FileNotFoundError as e:
    print("File not found...")
except Exception as e:
    print("Something went wrong! Message:\n{}".format(e))
else:
    print("Program executed succesfully. ")
finally:
    remove_if_exists(tmpfile_path)
    print("End of program. ")