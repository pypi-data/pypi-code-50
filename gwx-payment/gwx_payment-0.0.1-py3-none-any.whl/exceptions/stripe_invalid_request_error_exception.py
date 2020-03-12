from stripe.error import InvalidRequestError


class StripeInvalidRequestErrorException(InvalidRequestError):
    """Stripe specific exception implementation."""
    pass
