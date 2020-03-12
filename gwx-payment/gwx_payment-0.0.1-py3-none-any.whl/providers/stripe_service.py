import stripe
from stripe.error import InvalidRequestError
from gwx_payment.abstract_payment_service import AbstractPaymentService
from gwx_payment.exceptions.stripe_invalid_request_error_exception import StripeInvalidRequestErrorException


class StripeService(AbstractPaymentService):
    """Stripe API Service Wrapper

    Allow's you to send requests to Stripe's API using tokenized authentication.
    """

    def __init__(self, config: dict):
        super().__init__(config, stripe)
        self.service.api_key = self.config['api_key']

    def get_payment(self, payment_id: str) -> dict or None:
        """Returns a retrieved payment transaction based on the supplied payment id.

        :param payment_id: supplied from the previous stripe transaction, values varies from the ff:
            - `client_secret`
            - `publishable_key`
        :return: dict or None based on stripe's API Response.
        """
        try:
            return self.service.PaymentIntent.retrieve(payment_id)
        except InvalidRequestError:
            raise InvalidRequestError(f'InvalidRequestError id: {payment_id} does not exists.', payment_id)

    def confirm_payment(self, **kwargs) -> dict:
        """Confirm a payment will end the payment intent life cycle,
         by accepting the payment request of a user then marking it as paid.

         ie:
            payment_id: pi_1GGbV9COITrVsclWK5v3LFNx
            payment_method: card

        :param kwargs: MUST contains `payment_id` and `payment_method`.
        :return: dict or None based on stripe's API Response.
        """
        try:

            response = self.service.PaymentIntent.confirm(
                kwargs['payment_id'],
                payment_method=kwargs['payment_method']
            )

            return response

        except StripeInvalidRequestErrorException:
            raise StripeInvalidRequestErrorException('Error processing your confirm payment request.', [kwargs])

    def create_payment(self, **kwargs) -> dict:
        """Instantiate a payment intent.

        :param kwargs: listed parameters MUST exists:
            - amount
            - currency
            - payment_method
            - metadata = {}
        :return: dict or None based on stripe's API Response.
        """
        try:
            response = self.service.PaymentIntent.create(
                amount=kwargs['amount'],
                currency=kwargs['currency'],
                payment_method=kwargs['payment_method'],
                metadata={'integration_check': 'accept_a_payment'}
            )

            return response

        except StripeInvalidRequestErrorException:
            raise StripeInvalidRequestErrorException('Error processing your payment request.', [kwargs])
