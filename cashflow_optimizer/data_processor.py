import pandas as pd
from typing import Dict, Any
from data_fetcher import DataFetcher

class DataProcessor:
    """Processes and prepares financial data for optimization models.
    
    Attributes:
        fetcher: Instance of DataFetcher to get raw data.
    """
    
    def __init__(self):
        self.fetcher = DataFetcher()
        
    def process_data(self, data_type: str) -> pd.DataFrame:
        """Processes data based on type (stripe or plaid)."""
        if data_type == 'stripe':
            raw_data = self.fetcher.fetch_stripe_data()
        elif data_type == 'plaid':
            raw_data = self.fetcher.fetch_plaid_data()
        else:
            raise ValueError("Invalid data type")
            
        df = pd.DataFrame(raw_data)
        # Preprocess data: handle missing values, convert types
        try:
            df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
            df.dropna(inplace=True)
        except KeyError as e:
            logger.error(f"Key error in processing data: {str(e)}")
            raise
            
        return df