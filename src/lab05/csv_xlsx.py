import csv
from xlsxwriter import Workbook
from pathlib import Path
from .json_csv import check_errors


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Преобразует .csv файл в .xlsx.
    :param csv_path:
    :param xlsx_path:
    :return:
    """
    csv_path = Path(csv_path)
    xlsx_path = Path(xlsx_path)
    check_errors(csv_path, 'a.json', 'csv')
    wb = Workbook(xlsx_path)
    ws = wb.add_worksheet('Sheet1')

    with open(csv_path, encoding='utf-8') as f:
        reader = csv.reader(f)
        row = 0
        for row_data in reader:
            for col, cell in enumerate(row_data):
                ws.write(row, col, cell)
            row += 1
    wb.close()



if __name__ == "__main__":
    path = __file__[:__file__.find('src')] + 'data/lab05/'
    csv_to_xlsx(path + 'samples/people.csv', path + 'out/people_from_csv.xlsx')