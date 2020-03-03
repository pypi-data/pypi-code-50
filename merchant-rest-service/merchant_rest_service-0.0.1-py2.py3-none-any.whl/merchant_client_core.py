from .apibase import ApiBase
import json


class MerchantClientCore(ApiBase):

    def get_transaction_detail(self, reference_number):
        """
           Get Transaction Detail

           Parameters
           ----------
           reference_number : string
                reference_number The unique transaction code
                returned as part of a previously executed transaction

           Returns
           -------
           JSON Object
               JSON Object with the details of th transaction
           """

        endpoint = 'paga-webservices/merchant-rest/' \
                   'secured/getTransactionDetails'

        url = self._server_url() + endpoint

        pattern = reference_number

        generated_hash = self._generate_hash(pattern)

        data = {'referenceNumber': reference_number}

        json_data = json.dumps(data)

        response = self._post_request('POST', url, generated_hash, json_data)

        return response

    def get_transaction_detail_by_invoice_number(self, invoice_number):
        """
            Get Transaction Detail

            Parameters
            ----------
            invoice_number : string
                invoice_number The unique transaction code returned as
                 part of a previously executed transaction

            Returns
            -------
            JSON Object
                JSON Object with the details of the transaction
        """

        endpoint = 'paga-webservices/merchant-rest/secured/' \
                   'getTransactionDetailsByInvoiceNumber'

        url = self._server_url() + endpoint

        pattern = invoice_number

        generated_hash = self._generate_hash(pattern)

        data = {'invoiceNumber': invoice_number}

        json_data = json.dumps(data)

        response = self._post_request('POST', url, generated_hash, json_data)

        return response

    def get_process_detail(self, process_code):
        """
            Get Process details

            Parameters
            ----------
            process_code : string
                    process_code The process code returned as
                     part of a previously executed transaction
            Returns
            -------
            JSON Object
                JSON Object with the details of the transaction
        """

        endpoint = 'paga-webservices/merchant-rest/secured/getProcessDetails'

        url = self._server_url() + endpoint

        pattern = process_code

        generated_hash = self._generate_hash(pattern)

        data = {'processCode': process_code}

        json_data = json.dumps(data)

        response = self._post_request('POST', url, generated_hash, json_data)

        return response

    def get_foreign_exchange(self, base_currency, foreign_currency):
        """
         Get Foreign Exchange Rate

            Parameters
            ----------
                base_currency : string
                      base_currency the originating currency code
                foreign_currency : string
                      foreign_currency the currency code we
                       want to get the exchange rate for.
            Returns
            -------
        GetForeignExchangeRateResponse
        """
        endpoint = "paga-webservices/merchant-rest/" \
                   "secured/getForeignExchangeRate"

        url = self._server_url() + endpoint

        pattern = base_currency + foreign_currency

        generated_hash = self._generate_hash(pattern)

        data = {'baseCurrency': base_currency,
                'foreignCurrency': foreign_currency}
        json_data = json.dumps(data)
        response = self._post_request('POST', url, generated_hash, json_data)
        return response

    def get_reconciliation_report(self, period_start_date, period_end_date):
        """ Reconciliation Report

                Parameters
                ----------
                period_start_date : string
                 period_start_date The datetime period for
                 the reconciliation report to start
                period_end_date : string
                 period_end_date The datetime period for
                 the reconciliation report ends
                Returns
                -------
           ReconciliationReportResponse
        """

        endpoint = 'paga-webservices/merchant-rest/secured' \
                   '/reconciliationReport'

        url = self._server_url() + endpoint

        pattern = period_end_date + period_start_date

        generated_hash = self._generate_hash(pattern)

        data = {'periodStartDateTimeUTC': period_start_date,
                'periodEndDateTimeUTC': period_end_date}

        json_data = json.dumps(data)
        response = self._post_request('POST', url, generated_hash, json_data, )
        return response

    def refund_bill(self, reference_number, include_customer_fee,
                    full_refund, refund_amount, currency_code,
                    reason, customer_phone_number):
        """
        Refund Payment
             Parameters
                ----------
                reference_number: The unique reference number
                provided as part of the original transaction which
                identifies the transaction to be refunded.

                include_customer_fee:includesCustomerFee Indicates
                whether the refund includes the customer fee (true)
                 or not (false)

                full_refund:Indicates whether the refund is full or partial

                refund_amount: Only provided for a partial refund,
                 this indicates the amount to be refunded.

                currency_code: The currency used in the transaction.

                reason: Human readable reason for refund

                customer_phone_number: The phone number of the
                 customer that performed the operation

                Returns
                -------
                 ReconciliationReportResponse
        """

        endpoint = 'paga-webservices/merchant-rest/secured/refundBillPay'

        url = self._server_url() + endpoint

        pattern = reference_number + refund_amount + customer_phone_number

        generated_hash = self._generate_hash(pattern)

        data = {'referenceNumber': reference_number,
                'includesCustomerFee': include_customer_fee,
                'fullRefund': full_refund,
                'refundAmount': refund_amount,
                'currencyCode': currency_code,
                'reason': reason,
                'customerPhoneNumber': customer_phone_number}

        json_data = json.dumps(data)
        response = self._post_request('POST', url, generated_hash, json_data)
        return response

    def get_transaction_details_by_merchantreference(self, merchant_reference):
        """
            Get Process details

             Parameters
                ----------
                merchant_reference : string
                    merchant_reference The merchant unique
                     reference used to perform the transaction
            Returns
                -------
                JSON Object
                    JSON Object with the details of the transaction
        """

        endpoint = 'paga-webservices/merchant-rest/secured/' \
                   'getTransactionDetailsByMerchantReference'

        url = self._server_url() + endpoint

        pattern = merchant_reference

        generated_hash = self._generate_hash(pattern)

        data = {'merchantReference': merchant_reference}

        json_data = json.dumps(data)

        response = self._post_request('POST', url, generated_hash, json_data)

        return response
