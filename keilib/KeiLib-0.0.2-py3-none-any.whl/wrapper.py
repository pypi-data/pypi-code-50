import os
import json
import time
import requests
from Lib.config import APP_UID, APP_SECRET, TOKEN_FILE, REDIRECT_URI, SCOPE, STATE, HOOK
from flask import redirect



"""
    This is the main class for IntraLib. It contains the app_token handling
    and any other widely used function throughout the modules.
"""
class IntraLib:
    def __init__(self):
        if APP_UID == "None":
            raise EnvironmentError("APP_UID wasn't found in your .env file.")
        if APP_SECRET == "None":
            raise EnvironmentError("APP_SECRET wasn't found in your .env file.")
        if TOKEN_FILE == "None":
            raise EnvironmentError("TOKEN_FILE wasn't found in your .env file.")
        self.app_secret = APP_SECRET
        self.app_uid = APP_UID
        self.token_file = TOKEN_FILE
        self.app_token = IntraLib.check_app_token(self)
        self.redirect_uri = REDIRECT_URI
        self.scope = SCOPE
        self.state = STATE
        self.url = HOOK
        #self.user_token = IntraLib.check_user_token(self)


    """
        This function will request a new token to the 42 api.
        :return: Returns the newly requested token
    """
    def api_request_new_token(self):
        d = {'grant_type': 'client_credentials',
             'client_id': self.app_uid, 'client_secret': self.app_secret}
        r = requests.post("https://api.intra.42.fr/oauth/token", data=d)
        print("New access token requested.")
        print(r.json()['access_token'])
        with open(self.token_file, "w") as file:
            file.write(r.json()['access_token'])
        return r.json()['access_token']


    """
        This is used on the first route in the app, which would redirect
        to a second route based on :redirect_uri:
    """
    def code_redirect(self):
        d = {'client_id=' + self.app_uid, 'redirect_uri=' + self.redirect_uri,
            'response_type=' + 'code', 'scope=' + self.scope, 'state=' + self.state}
        print (d)
        r = redirect("https://api.intra.42.fr/oauth/authorize?%s" %
            ("&".join(d)))
        print (r)
        return r
    

    """
        This will request a token on behalf of the user who authorized
        the application. It requires a second route where you'll have
        to catch `code` argument and pass it to the function.
    """
    def api_request_user_token(self, code):
        d = {'grant_type': 'authorization_code',
            'client_id': self.app_uid, 'client_secret': self.app_secret,
            'code': code, "redirect_uri": self.redirect_uri}
        r = requests.post("https://api.intra.42.fr/oauth/token", data=d)
        print ("New user token was generated.")
        # with open(self.user_token_file, "w") as file:
        #     file.write(r.json()['access_token'])
        return r.json()['access_token']


    """
    This function will test on `/oauth/token/info` if the token is still
    available and hasn't expired.
    :return: Returns True if the token is still usable, False otherwise.
    """
    def test_token(self):

        self.app_token = IntraLib.get_token_from_file(self)
        h = {'Authorization': 'Bearer ' + self.app_token}
        r = requests.request("GET",
                             "https://api.intra.42.fr" + "/oauth/token/info", headers=h, allow_redirects=False)
        try:
            if r.json()['error'] == "invalid_request":
                return False
        except:
            pass
        return True


    """
    This function will get the token needed from the token file.
    :return: Returns the first line of the token file containing the
    app token.
    """
    def get_token_from_file(self):
        with open(self.token_file, 'r+') as file:
            return file.readline()


    """
    This function will get the authenticated user token from the self_token file.
    :return: Returns the first line of the file containing the self token.
    """
    def get_self_token(self):
        with open(self.user_token, 'r+') as file:
            return file.readline()


    """
    This function will check every possible case of error possible with
    the app token:
    If the file doesn't exists
    If the file is empty
    If the token is expired/incomplete
    :return: Returns the app_token string
    """

    def check_app_token(self):
        if os.path.exists(TOKEN_FILE):
            if os.stat(TOKEN_FILE).st_size != 0:
                if IntraLib.test_token(self):
                    self.app_token = IntraLib.get_token_from_file(self)
                else:
                    self.app_token = IntraLib.api_request_new_token(self)
            else:
                self.app_token = IntraLib.api_request_new_token(self)
        else:
            open(self.token_file, 'a').close()
            self.app_token = IntraLib.api_request_new_token(self)
        with open(self.token_file, "w") as file:
            file.write(str(self.app_token))
        return self.app_token


    # def check_user_token(self):
    #     if os.path.exists(USER_TOKEN_FILE):
    #         if os.stat(USER_TOKEN_FILE).st_size != 0:
    #             if IntraLib.test_user(self):
    #                 self.user_token = IntraLib.get_user_token(self)
    #             else:
    #                 self.user_token = IntraLib.api_request_user_token(self)
    #         else:
    #             open(self.user_token_file, 'a').close()
    #             self.user_token = IntraLib.api_request_self_token(self)
    #         with open(self.user_token_file, "w") as file:
    #             file.write(str(self.user_token_file))
    #         return self.user_token

    """
    This function will handle all the API requests.
    If the token suddenly expires, this function will call check_token
    and then recursively call itself again until the token works.
    :param args: Arguments passed to the request
    :param uri: The url you want to request from
    :param methods: The method you want to to your API request on. By default, `methods` is set to `GET`
    :return: Returns the response object returned by requests.request()
    """
    def api_get(self, uri: str, args, methods="GET"):
        result = []
        fixed_parameters = self.get_fixed_parameters(args)
        h = {'Authorization': 'Bearer ' + self.app_token}
        # try:
        while args.from_page <= args.to_page:
            response = requests.request(methods, "https://api.intra.42.fr" + str(uri) + self.get_changeable_parameters(args) + fixed_parameters, headers=h, allow_redirects=False)
            if response.status_code == 401:
                self.app_token = IntraLib.check_app_token(self)
                return IntraLib.api_get(self, uri, args, methods)
            elif response.status_code == 403 or response.status_code == 429:
                time.sleep(int(response.headers["Retry-After"]))
                continue
            ret = json.loads(response.content)
            # print (response.content)
            if not ret:
                break
            i = 0
            while i < len(ret):
                result.append(ret[i])
                i += 1
            args.from_page += 1
        return result
        # except Exception as badgateway:
        #     return print ("Intra is down so this error message is shown to you. :(")
        #     slack.send(text="Exception hapened due to intra being down.")


    """
    This function will handle all the API requests that send a single json response back.
    If the token suddenly expires, this function will call check_token
    and then recursively call itself again until the token works.
    :param uri: The url you want to request from
    :param methods: The method you want to to your API request on. By default, `methods` is set to `GET`
    :return: Returns the response object returned by requests.request()
    """
    def api_get_single(self, uri: str, methods="GET"):
        h = {'Authorization': 'Bearer ' + self.app_token}
        response = requests.request(methods, "https://api.intra.42.fr" +
                             uri, headers=h, allow_redirects=False)
        if response.status_code == 401:
            self.app_token = IntraLib.check_app_token(self)
            return IntraLib.api_get_single(self, uri, methods)
        elif response.status_code == 403 or response.status_code == 429:
            time.sleep(int(response.headers["Retry-After"]))
            return self.api_get_single(uri, methods)
        return response


    """
    This will create and return the string with the parameter that will
    change regularly (the page).
    :param args: The arguments used to get the `from_page` variable
    :return: Returns a string that is appened to the url sent to the api
    """
    def get_changeable_parameters(self, args):
        return "?" + "page[number]=" + str(args.from_page)


    """
    This function will add the strings together to form the part of the url
    where it wont change. This part of the url contains the sorts,
    filters etc...
    :param args: The arguments to add in the url
    :return: Returns a string that is appened to the url sent to the api
    """
    def get_fixed_parameters(self, args):
        fixed_parameters = "&page[size]=" + str(args.page_size)
        if type(args.sort) == str:
            fixed_parameters += "&sort=" + str(args.sort)
        if type(args.filter) == str:
            fixed_parameters += "&filter" + str(args.filter)
        if type(args.range) == str:
            fixed_parameters += "&range" + str(args.range)
        return fixed_parameters


    """
    This function will return the uid of the token from /oauth/token/info
    :return: Returns the uid in a string form.
    """
    def get_uid_from_token(self):
        response = self.api_get_single("/oauth/token/info")
        ret = json.loads(response.content)
        return str(ret["application"]["uid"])


    """
    This function will return in how many seconds will the token expire.
    :return: Return the time in seconds of when the token will expire
    """
    def get_token_expire_time_in_seconds(self):
        response = self.api_get_single("/oauth/token/info")
        ret = json.loads(response.content)
        return str(ret["expires_in_seconds"])


    """
    This function will return in hours:minutes:seconds the time of expiry of the token.
    :return: Returns a string formated in h:m:s
    """
    def get_token_expire_time(self):
        response = self.api_get_single("/oauth/token/info")
        ret = json.loads(response.content)
        m, s = divmod(ret["expires_in_seconds"], 60)
        h, m = divmod(m, 60)
        return str("%d:%02d:%02d" % (h, m, s))


    """
    This function will return the epoch time of creation of the token.
    :return: Returns a string containing the epoch creation time
    """
    def get_token_creation_epoch(self):
        response = self.api_get_single("/oauth/token/info")
        ret = json.loads(response.content)
        return str(ret["created_at"])


    """
    This function will return the date and time of creation for the token.
    :return: It will return a string in form of `YYYY-MM-DD hh-mm-ss`
    """
    def get_token_creation_date(self):
        response = self.api_get_single("/oauth/token/info")
        ret = json.loads(response.content)
        return str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ret["created_at"])))

    
    """
    This is for handling my Slack notifications.
    """
    def send(self, **kwargs):
        self.headers = {"Content-type": "application/json"}
        data = json.dumps(kwargs).encode()
        ret = requests.post(self.url, data=data, headers=self.headers)
        if ret.status_code != 200:
            raise ValueErrorError(
            'Request to slack returned an error %s, response is:\n%s'
            % (ret.status_code, ret.text)
            )