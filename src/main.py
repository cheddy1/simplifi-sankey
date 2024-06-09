from .csv_handler import TransationData


def main(file_names: list[str]):
    transaction_data = TransationData(file_names)
    transaction_data.read_transaction_csv()
    transaction_data.clean_transaction_data()
    transaction_data.generate_sankey_str()
