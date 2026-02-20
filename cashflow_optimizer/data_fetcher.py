import os
import logging
from typing import Dict, Any
import requests

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DataFetcher:
    """Fetches financial data from external APIs and internal systems.
    
    Attributes:
        api_keys: Dictionary containing API keys for Stripe, Plaid, etc.
        base_url: Base URL for API requests.
    """
    
    def __init__(self):
        self.api_keys = {
            'stripe': os.getenv('STRIPE_API_KEY'),
            'plaid': os.getenv('PLAID_API_KEY')
        }
        
    def fetch_stripe_data(self) -> Dict[str, Any]:
        """Fetches transaction data from Stripe API."""
        try:
            response = requests.get(
                f"{self.base_url}/stripe/transactions",
                headers={'Authorization': f'Bearer {self.api_keys["stripe"]}'}
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Stripe API request failed: {str(e)}")
            raise
        
    def fetch_plaid_data(self) -> Dict[str, Any]:
        """Fetches account balance data from Plaid API."""
        try:
            response = requests.get(
                f"{self.base_url}/plaid/balances",
                headers={'Authorization': f'Bearer {self.api_keys["plaid"]}'}
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Plaid API request failed: {str(e)}")
            raise