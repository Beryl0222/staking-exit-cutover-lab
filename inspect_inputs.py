"""列出资料表及其实际记录数，保留源表字段供人工核对。"""
import argparse
import csv
from pathlib import Path


def read_table(directory, name):
    """返回未经业务解释的 CSV 源记录。"""
    with (directory / (name + ".csv")).open(encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return reader.fieldnames, list(reader)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", nargs="?", type=Path, default=Path("data"),
                        help="包含 CSV 资料的目录")
    args = parser.parse_args()
    for path in sorted(args.directory.glob("*.csv")):
        fields, records = read_table(args.directory, path.stem)
        print(f"{path.stem}\t{len(records)}\t{','.join(fields)}")


if __name__ == "__main__":
    main()
