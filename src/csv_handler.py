import csv
from collections import defaultdict
from re import sub
from decimal import Decimal
from .utils.consts import *


class TransationData:
    def __init__(self, file_names_list: list[str]):
        self.file_names_list = file_names_list
        self.raw_categories = defaultdict(lambda: 0)
        self.clean_categories = defaultdict(lambda: 0)
        self.category_pairs = defaultdict(list)

    def read_transaction_csv(self):
        for file_name in self.file_names_list:
            if len(self.file_names_list) == 1 or "example_export" not in file_name:
                with open(file_name) as file:
                    csv_file = csv.DictReader(file)
                    for row in csv_file:
                        self.raw_categories[row["category"]] += Decimal(
                            sub(r"[^\d\-.]", "", row["amount"])
                        )

    def clean_transaction_data(self):
        for raw_category in self.raw_categories:
            if raw_category in ROOT_CATEGORIES:
                self.clean_categories[raw_category] += self.raw_categories[raw_category]
            if ":" in raw_category:
                sub_category = sub(r".*?:", "", raw_category)
                parent_category = sub(r":.*", "", raw_category)
                self.category_pairs[parent_category].append(sub_category)
                self.clean_categories[sub_category] += self.raw_categories[raw_category]

    def generate_sankey_str(self):
        report = ""
        for root_category in self.clean_categories:
            if root_category in self.category_pairs:
                for sub_category in self.category_pairs[root_category]:
                    report += (
                        f"{root_category} [{self.clean_categories[sub_category]}] {sub_category}"
                    )
                    report += "\n"
        print(report)
