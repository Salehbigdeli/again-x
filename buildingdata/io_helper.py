import os
import fileinput
import zipfile
from urllib.request import urlretrieve
from os.path import basename
from urllib.request import urlopen


def merge_csvs(dir_name, out_name):
    with open(out_name, 'w') as fout:
        files = [os.path.join(dir_name, f) for f in os.listdir(dir_name)]
        fin = fileinput.input(files)
        for line in fin:
            fout.write(line)
        fin.close()


def unzip(file_name, to):
    with zipfile.ZipFile(file_name, 'r') as zipf:
        zipf.extractall(to)


def download(url):
    resp = urlopen(url)
    file_name = basename(resp.url)
    res = urlretrieve(resp.url, file_name)
    return res[0]


def read_data(url):
    file = download(url)
    unzip(file, './data')
    return './data', file
