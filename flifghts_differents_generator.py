#!/venv/bin/env python3


from xml.etree import ElementTree as ET
# from pandas import DataFrame
import os


def get_file_names():
    data_dir = 'data'
    file_names = os.listdir(data_dir)
    files_path = [
        os.path.abspath(os.path.join(data_dir, file_name))
        for file_name in file_names if file_name.endswith('.xml')
    ]

    if len(files_path) != 2:
        raise ValueError("Необходимо два xml-файла для сравнения")

    return files_path


def load_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root


def parse_xml(root):
    pass


def main():
    try:
        file_path_1, file_path_2 = get_file_names()
    except ValueError as e:
        print(e)
        return
    #  xml_1 = parse_xml(load_xml(file_path_1))
    #  xml_2 = parse_xml((load_xml(file_path_2))
    #  парсинг xml-файлов


if __name__ == '__main__':
    main()
