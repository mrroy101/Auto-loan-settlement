from pathlib import Path
import pandas as pd


class CustomerWorkbookService:
    def load(self, customer_id: str):
        workbook_path = Path('data') / f'{customer_id}.xlsx'
        return pd.ExcelFile(workbook_path)
