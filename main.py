import os
import shutil

from buildingdata.csv_creator import convert_buildings_to_csv
from buildingdata.io_helper import read_data, merge_csvs


def convert(url, clean_intermediate=True):
    path, file = read_data(url)
    converted_chunks = convert_buildings_to_csv(path)
    merge_csvs(converted_chunks, f'{file}_buldings.csv')
    if clean_intermediate:
        shutil.rmtree(path)
        os.remove(file)


if __name__ == '__main__':
    convert('https://www.data.gouv.fr/fr/datasets/r/35ef7be3-8a26-42ee-9003-f9240b84453f')
    convert('https://www.data.gouv.fr/fr/datasets/r/ca672276-008f-481d-9647-e9ab93c92132')

