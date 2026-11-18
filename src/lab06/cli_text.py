import argparse
from pathlib import Path
from ..lab03.text_stats import table

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5, help="Количество слов для сводки, изначально 5")

    args = parser.parse_args()

    file_path = (Path(__file__).resolve().parent / args.input).resolve()

    try:
        if args.command == "cat":
            with open(file_path, encoding='utf-8') as file:
                line_num = 0
                for line in file:
                    line_num += 1
                    if args.n:
                        print(f'{line_num} {line.strip()}')
                    else:
                        print(line.strip())
        elif args.command == "stats":
            with open(file_path, encoding='utf-8') as file:
                table(file.read(), needs_tokenizing=True, top=args.top)
    except OSError:
        parser.error(f'Invalid path: {file_path}')


if __name__ == '__main__':
    main()