import json, csv
from pathlib import Path

def check_errors(json_path, csv_path, file_type):
    if json_path.suffix != '.json':
        raise ValueError('Файл не типа JSON.')
    if csv_path.suffix != '.csv':
        raise ValueError('Файл не типа CSV.')
    read_path = json_path if file_type == 'json' else csv_path
    if read_path.exists():
        with open(read_path, encoding='utf-8') as read_file:
            if read_file.read().strip() == '':
                raise ValueError(f'Файл {file_type.upper()} пустой.')
    else:
        raise FileNotFoundError(f'Файл {file_type.upper()} не существует.')


def json_to_csv(json_path: Path|str, csv_path: Path|str):
    """Превращает json в csv."""
    json_path = Path(json_path)
    csv_path = Path(csv_path)
    check_errors(json_path, csv_path, 'json')
    with open(json_path, encoding="utf-8") as json_file:
        try:
            json_res = json.load(json_file)
        except json.decoder.JSONDecodeError:
            raise
    with open(csv_path, mode="w", encoding="utf-8", newline='') as csv_file:
        csv_res = csv.DictWriter(csv_file, fieldnames=json_res[0].keys())
        csv_res.writeheader()
        for row in json_res:
            csv_res.writerow(row)

def csv_to_json(csv_path, json_path):
    """Превращает csv в json."""
    json_path = Path(json_path)
    csv_path = Path(csv_path)
    check_errors(json_path, csv_path, 'csv')
    with open(csv_path, encoding='utf-8') as csv_file:
        csv_res = list(csv.DictReader(csv_file))
        if not all([None not in set(list(i.keys())) for i in csv_res]):
            raise ValueError('Пустой заголовок CSV.')
    with open(json_path, mode='w', encoding='utf-8') as json_file:
        json.dump(csv_res, json_file, ensure_ascii=False, indent=2)


# test cases
if __name__ == '__main__':
    path = __file__[:__file__.find('src')] + 'data/lab05/'
    csv_to_json(path + 'samples/people.csv', path + 'out/people_from_csv.json')
    json_to_csv(path + 'samples/people.json', path + 'out/people_from_json.csv')

