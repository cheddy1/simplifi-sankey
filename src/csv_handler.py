import csv
from collections import defaultdict
import locale
from re import sub
from decimal import Decimal


class TransationData:
    def __init__(self, file_names_list: list[str]):
        self.file_names_list = file_names_list
        self.categories = defaultdict(lambda: 0)

    def read_transaction_csv(self):
        for file_name in self.file_names_list:
            with open(file_name) as file:
                csv_file = csv.DictReader(file)
                for row in csv_file:
                    self.categories[row["category"]] += Decimal(sub(r"[^\d\-.]", "", row["amount"]))

        print(self.categories)
