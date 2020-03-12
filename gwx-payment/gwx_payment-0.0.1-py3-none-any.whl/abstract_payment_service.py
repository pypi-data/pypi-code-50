from abc import abstractmethod


class AbstractPaymentService:
    # The service that will be defined in each of the concrete provider class
    service = None

    # The defined configuration file
    config: dict = None

    def __init__(self, config: dict, service: object):
        self.config = config
        self.service = service

    @abstractmethod
    def confirm_payment(self, **kwargs) -> dict:
        """Confirm the payment, this states that the payment has been accepted,
        and sent to the vendor.

        :param kwargs: named payload parameters
        :return: structured value required for response composition.
        """
        pass

    @abstractmethod
    def create_payment(self, **kwargs) -> dict:
        """Checkout method, this will initiate the payment transaction.

        :param kwargs: the parameters for the payment creation.
        :return: structured value required for response composition.
        """
        pass

    @abstractmethod
    def get_payment(self, payment_id: str) -> dict or None:
        """Retrieve a specific payment record

        :param payment_id: the primary id used to reference against an endpoint.
        :return: the retrieved record, null if none found.
        """
        pass
