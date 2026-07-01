from pathlib import Path
import pandas as pd

from utils.constants import MASTER_FILE_NAME
from utils.exceptions import CustomerNotFoundException


class CustomerMasterService:

    def __init__(self, data_folder: str = "data"):
        self.master_file = Path(data_folder) / MASTER_FILE_NAME
        self.df = pd.read_excel(self.master_file)

    def get_all_customers(self):
        return self.df

    def get_customer(self, customer_id: str):
        customer = self.df[self.df["Customer ID"] == customer_id]

        if customer.empty:
            raise CustomerNotFoundException(f"Customer {customer_id} not found.")

        return customer.iloc[0]

    def search_customer(self, keyword: str):
        keyword = keyword.lower()
        return self.df[self.df["Customer Name"].str.lower().str.contains(keyword)]
