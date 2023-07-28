import os
import itertools as it

def scantree(path):
    for elem in os.scandir(path):
        if elem.is_dir() == True:
            yield elem
            yield from scantree(elem.path)
        else:
            yield elem

listing = scantree("/home/tomek/Projects/tutorials-python/Python/udemy_python_mid_advanced_mobilo")

# for element in listing:
#     if element.is_dir():
#         dir_or_file = "dir "
#     elif element.is_file():
#         dir_or_file = "file"
#     else:
#         dir_or_file = "other?"
#     print("{} - {}".format(dir_or_file, element.path))
#     # quick, without other: print('DIR ' if element.is_dir() else 'FILE', element.path)

listing = scantree("/home/tomek/Projects/tutorials-python/Python/udemy_python_mid_advanced_mobilo")
listing = sorted(listing, key=lambda x: x.is_dir())

for is_dir, elements in it.groupby(listing, key=lambda x: x.is_dir()):
    print('DIR ' if is_dir else 'FILE', len(list(elements)))
