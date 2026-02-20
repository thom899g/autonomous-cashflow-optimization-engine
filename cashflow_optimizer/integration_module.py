import stripe
from plaid import PlaidClient
from typing import Dict, Any

class IntegrationModule:
    """Handles integration with Stripe and Plaid APIs.
    
    Attributes:
        stripe_key: API key for Stripe integration.
        plaid_client: Instance of Plaid client.
    """
    
    def __init__(self):
        self.stripe = stripe.Stripe(api_key=os.getenv('STRIPE_API_KEY'))
        self.plaid = PlaidClient(os.getenv('PLAID_API_KEY'))
        
    def process_transaction(self, transaction_data: Dict[str, Any]) -> Dict[str, Any]:
        """Processes a transaction using Stripe."""
        try:
            response = self.stripe.payment_intent.create(
                amount=transaction_data['amount'],
                currency=transaction_data['currency']
            )
            return {'status': 'success', 'intent_id': response.id}
        except stripe.error.StripeError as e:
            logger.error(f"Stripe transaction failed: {str(e)}")
            raise