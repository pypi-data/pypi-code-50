from .. import __request as request
from ..__authorize_creds import authorize
from .__bank_det_valid import BankDetailsValidation
from .__upi_validation import UPIValidation
from .__bulk_bank_validation import BulkBankValidation
from .__get_bulk_bank_valid_status import GetBulkBankValidationStatus


class Validations:
    
    @staticmethod
    @authorize
    def bank_details_validation(bankAccount, ifsc, name, phone):
        r""" Validate bank details by penny drop.
        :param bankAccount: bankAccount.
        :param ifsc: ifsc.
        :param name: name.
        :param phone: phone.
        :return: :class:`Response <Response>` object.
        :rtype: requests.Response.
        """
        bank_det_valid_req = BankDetailsValidation(bankAccount=bankAccount, ifsc=ifsc, 
            name=name, phone=phone)
        return request.trigger_request(bank_det_valid_req)

    @staticmethod
    @authorize
    def upi_validation(name, vpa):
        r""" Validate upi details by penny drop.
        :param name: name.
        :param vpa: vpa.
        :return: :class:`Response <Response>` object.
        :rtype: requests.Response.
        """
        upi_valid_req = UPIValidation(name=name, vpa=vpa)
        return request.trigger_request(upi_valid_req)

    @staticmethod
    @authorize
    def bulk_bank_validation(bulkValidationId, entries):
        r""" Validate bulk bank details by penny drop.
        :param bulkValidationId: bulkValidationId.
        :param entries: entries.
        :return: :class:`Response <Response>` object.
        :rtype: requests.Response.
        """
        bulk_bank_valid_req = BulkBankValidation(bulkValidationId=bulkValidationId, entries=entries)
        return request.trigger_request(bulk_bank_valid_req)

    @staticmethod
    @authorize
    def get_bulk_bank_validation_status(bulkValidationId, **kwargs):
        r""" Get bulk bank validation status.
        :param bulkValidationId: bulkValidationId.
        :param entries: entries.
        :return: :class:`Response <Response>` object.
        :rtype: requests.Response.
        """
        get_bulk_valid_status_req = GetBulkBankValidationStatus(bulkValidationId=bulkValidationId, **kwargs)
        return request.trigger_request(get_bulk_valid_status_req)
