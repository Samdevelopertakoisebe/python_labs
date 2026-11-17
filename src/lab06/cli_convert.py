import argparse
from ...src.lab05.json_csv import json_to_csv, csv_to_json
from ...src.lab05.csv_xlsx import csv_to_xlsx
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    in_path = (Path(__file__).resolve().parent / args.input).resolve()
    out_path = (Path(__file__).resolve().parent / args.output).resolve()
    if args.cmd == "json2csv":
        json_to_csv(in_path, out_path)
    if args.cmd == "csv2json":
        csv_to_json(in_path, out_path)
    if args.cmd == "csv2xlsx":
        csv_to_xlsx(in_path, out_path)


if __name__ == "__main__":
    main()