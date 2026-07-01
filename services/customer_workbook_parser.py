import pandas as pd


class CustomerWorkbookParser:
    def parse(self, customer_sheet):
        customer_data = {}
        for _, row in customer_sheet.iterrows():
            field = row[0]
            value = row[1]
            customer_data[field] = value
        return customer_data, None, None
