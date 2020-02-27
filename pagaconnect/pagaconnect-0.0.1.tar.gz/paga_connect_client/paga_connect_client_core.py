from .apibase import ApiBase


class PagaConnectCore(ApiBase):

    def get_access_token(self, authorization_code, redirect_uri, scope,
                         user_data):
        """
        Gets the access token

        Parameters
        ----------
        authorization_code : string
            authorization code received from user's approval of
            Merchant's access to their Paga account
        redirect_uri : string
            Where Merchant would like the user to the redirected to after
            receiving the access token
        scope : string
            List of activities to be performed with the access token
        user_data : string
            List of user data data to be collected

        Returns
        -------
        JSON Object
            JSON Object with access token inside
        """
        server_url = self._server_url()

        access_token_url = server_url + "/paga-webservices/oauth2/token?"
        full_url = "{0}grant_type=authorization_code&redirect_uri={1}" \
                   "&code={2}&scope={3}&user_data={4}" \
            .format(access_token_url, redirect_uri,
                    authorization_code, scope, user_data)

        response = self._post_request('POST', full_url, None)

        return response

    def make_payment(self, access_token, reference_number,
                     amount, user_id, product_code, currency):

        """ Make payment

             Parameters
             ----------
             access_token : string
                 User's access token
             reference_number : string
                 A unique reference number provided by the client to uniquely
                 identify the transaction
             amount : float
                 Amount to charge the user
             user_id : string
                 A unique identifier for merchant's customer
             product_code : string
                 Optional identifier for the product/service to be bought
             currency : string
                 he currency code of the transaction, NGN is the only supported
                 currency as of now (February 2016)

             Returns
             -------
             JSON Object
                 JSON Object with access token inside
             """
        server_url = self._server_url()
        print(server_url)
        payment_url = server_url + "/paga-webservices/oauth2/" \
                                   "secure/merchantPayment"
        print(payment_url)

        if currency is None:
            payment_link = payment_url + "/referenceNumber" + \
                           str(reference_number) + "/amount/" + str(amount) + \
                           "/merchantCustomerReference/" + str(user_id) \
                           + "/merchantProductCode/" + str(product_code)
        elif currency is None and product_code is None:
            payment_link = payment_url + "/referenceNumber/" + \
                           str(reference_number) + "/amount/" + str(amount) + \
                           "/merchantCustomerReference/" + str(user_id)
        else:
            payment_link = payment_url + "/referenceNumber/" + \
                           str(reference_number) + "/amount/" + str(amount) + \
                           "/merchantCustomerReference/" + str(user_id) + \
                           "/merchantProductCode" + "/" + str(product_code) \
                           + "/currency/" + str(currency)

        response = self._post_request('POST', payment_link, access_token)

        return response

    def money_transfer(self, access_token, reference_number, amount,
                       skip_messaging, recipient_credential):

        server_url = self._server_url()

        money_transfer_url = server_url + "/paga-webservices/oauth2/secure" \
                                          "/moneyTransfer/v2?"

        money_transfer_request_url = money_transfer_url \
                                     + "amount=" + str(amount) \
                                     + "&referenceNumber=" + reference_number \
                                     + "&skipMessaging=" + str(skip_messaging) \
                                     + "&recipientCredential=" + recipient_credential

        response = self._post_request('POST', money_transfer_request_url, access_token)

        return response

    def get_user_details(self, access_token):

        server_url = self._server_url()

        user_detail_url = server_url + "/paga-webservices/oauth2/" \
                                       "secure/getUserDetails"

        response = self._post_request('POST', user_detail_url, access_token)

        return response
