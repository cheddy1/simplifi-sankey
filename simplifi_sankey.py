import argparse
import os
from src.main import main


def parse_args() -> None:
    parser = argparse.ArgumentParser(
        prog="Simplifi Sankey",
        description="Generates a sankey from your simplifi transaction output!",
    )
    parser.add_argument("-f", "--file", help=".csv file of transaction data", type=str)
    args = parser.parse_args()
    file_names = args.file
    if not file_names:
        file_names = [
            os.path.join(dirpath, f)
            for (dirpath, dirnames, filenames) in os.walk("data")
            for f in filenames
        ]
    else:
        file_names = [file_names]
    main(file_names)


if __name__ == "__main__":
    parse_args()
