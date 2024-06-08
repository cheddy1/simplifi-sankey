from .csv_handler import TransationData


def main(file_names: list[str]):
    transaction_data = TransationData(file_names)
    transaction_data.read_transaction_csv()
