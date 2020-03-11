from collections import OrderedDict


class DataOrdered:
    def __init__(self):
        pass

    @staticmethod
    def get_sheba_info_and_status():
        data = OrderedDict()
        data["UserName"] = ""
        data["Sheba"] = ""
        data["ShenaseVariz"] = ""
        data["Timestamp"] = ""
        return data

    @staticmethod
    def get_deposit_number_by_card_number():
        data = OrderedDict()
        data["UserName"] = ""
        data["CardNumber"] = ""
        data["Timestamp"] = ""
        return data

    @staticmethod
    def get_sheba_by_card_number():
        data = OrderedDict()
        data["UserName"] = ""
        data["CardNumber"] = ""
        data["Timestamp"] = ""
        return data

    @staticmethod
    def get_card_information():
        data = OrderedDict()
        data["UserName"] = ""
        data["SrcCardNumber"] = ""
        data["DestCardNumber"] = ""
        data["Timestamp"] = ""
        return data

    @staticmethod
    def card_to_card():
        data = OrderedDict()
        data["UserName"] = ""
        data["SrcCardNumber"] = ""
        data["DestCardNumber"] = ""
        data["Password"] = ""
        data["Cvv2"] = ""
        data["ExpireMonth"] = ""
        data["ExpireYear"] = ""
        data["Amount"] = ""
        data["Email"] = ""
        data["AuthorizationCode"] = ""
        data["WithReferenceNumber"] = ""
        data["CardName"] = ""
        data["SrcComment"] = ""
        data["DestComment"] = ""
        data["OriginalAddress"] = ""
        data["JsonData"] = ""
        data["Timestamp"] = ""
        return data

    @staticmethod
    def card_to_card_list():
        data = OrderedDict()
        data["UserName"] = ""
        data["SourceCardNumber"] = ""
        data["SourceDepositNumber"] = ""
        data["DestinationCardNumber"] = ""
        data["MinAmount"] = ""
        data["MaxAmount"] = ""
        data["StartDate"] = ""
        data["EndDate"] = ""
        data["RefrenceNumber"] = ""
        data["SequenceNumber"] = ""
        data["SourceNote"] = ""
        data["DestinationNote"] = ""
        data["Timestamp"] = ""
        return data

    @staticmethod
    def get_submission_cheque():
        data = OrderedDict()
        data["UserName"] = ""
        data["Deposit"] = ""
        data["ChequeNumber"] = ""
        data["MinAmount"] = ""
        data["MaxAmount"] = ""
        data["StartDate"] = ""
        data["EndDate"] = ""
        data["BankCode"] = ""
        data["ChequeStatus"] = ""
        data["StartSubmisionDate"] = ""
        data["EndSubmissionDate"] = ""
        data["RowCount"] = ""
        data["Timestamp"] = ""
        return data

    @staticmethod
    def convert_deposit_number_to_sheba():
        data = OrderedDict()
        data["UserName"] = ""
        data["DepositNumber"] = ""
        data["Timestamp"] = ""
        return data

    @staticmethod
    def convert_sheba_to_deposit_number():
        data = OrderedDict()
        data["UserName"] = ""
        data["Sheba"] = ""
        data["Timestamp"] = ""
        return data

    @staticmethod
    def paya_service():
        data = OrderedDict()
        data["UserName"] = ""
        data["SourceDepositNumber"] = ""
        data["FileUniqueIdentifier"] = ""
        data["TransferMoneyBillNumber"] = ""
        data["BatchPayaItemInfos"] = ""
        data["Timestamp"] = ""
        return data

    @staticmethod
    def get_deposit_invoice():
        data = OrderedDict()
        data["UserName"] = ""
        data["DepositNumber"] = ""
        data["Sheba"] = ""
        data["StartDate"] = ""
        data["EndDate"] = ""
        data["FirstIndex"] = ""
        data["Count"] = ""
        data["Timestamp"] = ""
        return data

    @staticmethod
    def get_deposit_balance():
        data = OrderedDict()
        data["UserName"] = ""
        data["DepositNumber"] = ""
        data["Sheba"] = ""
        data["Timestamp"] = ""
        return data

    @staticmethod
    def transfer_money():
        data = OrderedDict()
        data["UserName"] = ""
        data["SourceDepositNumber"] = ""
        data["SourceSheba"] = ""
        data["DestDepositNumber"] = ""
        data["DestSheba"] = ""
        data["DestFirstName"] = ""
        data["DestLastName"] = ""
        data["Amount"] = ""
        data["SourceComment"] = ""
        data["DestComment"] = ""
        data["PaymentId"] = ""
        data["Timestamp"] = ""
        return data

    @staticmethod
    def get_transfer_state():
        data = OrderedDict()
        data["UserName"] = ""
        data["Date"] = ""
        data["PaymentId"] = ""
        data["Timestamp"] = ""
        return data

    @staticmethod
    def bill_payment_by_deposit():
        data = OrderedDict()
        data["UserName"] = ""
        data["PaymentId"] = ""
        data["DepositNumber"] = ""
        data["BillNumber"] = ""
        data["Timestamp"] = ""
        return data

    @staticmethod
    def get_card_information_by_card_info():
        data = OrderedDict()
        data["UserName"] = ""
        data["SrcCardNumber"] = ""
        data["DestCardNumber"] = ""
        data["Cvv2"] = ""
        data["ExpireMonth"] = ""
        data["ExpireYear"] = ""
        data["Pin2"] = ""
        data["Timestamp"] = ""
        return data



