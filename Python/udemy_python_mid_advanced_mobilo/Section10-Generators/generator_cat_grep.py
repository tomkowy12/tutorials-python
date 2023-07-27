import os 
import requests

DIR_LOCATION = "/home/tomek/Projects/tutorials-python/Python/udemy_python_mid_advanced_mobilo/Section10-Generators/links_to_check"

def gen_get_files(dir):
    for file in os.listdir(dir):
        yield os.path.join(dir, file)

def gen_get_file_lines(filename):
    with open(filename, "r") as f:
        for line in f.readlines():
            yield line.replace("\n", "")

def check_webpage(url):
    try:
        with open(requests.get(url)) as page:
            return page.status_code == 200
    except Exception as e:
        print(e)
        return False
    try:
        response = requests.get(url)
        return response.status_code == 200
    except:
        return False

def create_files(): 
    try:
        os.mkdir(DIR_LOCATION)
    except:
        pass
    
    with open(DIR_LOCATION + "/pl.txt", "w") as f:
        f.write('http://www.wykop.pl/\n')
        f.write('http://www.ale-beka-jest-taki-adres.pl/\n')
        f.write('http://www.demotywatory.pl')
    
    with open(DIR_LOCATION + "/com.txt", "w") as f:
        f.write('http://www.realpython.com/\n')
        f.write('http://www.nonexistenturl.com/\n')
        f.write('http://www.stackoverflow.com')

# create_files()

for file in gen_get_files(DIR_LOCATION):
    for line in gen_get_file_lines(file):
        print("{} - {} - {}".format(file, line, check_webpage(line)))