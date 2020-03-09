# -*- coding: utf-8 -*-
import urllib.request
import json

class CustomersMailCloud:
    def __init__(self, api_user, api_key):
        if (api_user is None or api_user == ''):
            raise Exception('API User is required.')
        if (api_key is None or api_key == ''):
            raise Exception('API Key is required.')
        self.endpoints = {
            "trial": "https://sandbox.smtps.jp/api/v2/emails/send.json",
            "standard": "https://te.smtps.jp/api/v2/emails/send.json",
            "pro": "https://SUBDOMAIN.smtps.jp/api/v2/emails/send.json"
        }
        self.api_user = api_user
        self.api_key = api_key
        self.url = "";
        self.to_address = [];
        self.from_address = {};
        self.subject = '';
        self.text = '';
        self.html = '';
        self.attachments = [];

    def trial(self):
        self.url = self.endpoints['trial'];
    def standard(self):
        self.url = self.endpoints['standard'];
    def pro(self, subdomain):
        if (subdomain is None or subdomain == ''):
            raise Exception('サブドメインは必須です')
        self.url = self.endpoints['pro'].replace('SUBDOMAIN', subdomain)
    def addTo(self, name, address):
        self.to_address.append({
            'name': name,
            'address': address
        })
    def setFrom(self, name, address):
        self.from_address = {
            'name': name,
            'address': address
        }
    def send(self):
        if (self.url == ''):
             raise Exception('契約プランを選択してください（trial/standard/pro）')
        if (self.from_address['address'] is None or self.from_address['address'] == ''):
            raise Exception('送信元アドレスは必須です')
        if (len(self.to_address) == 0):
            raise Exception('送り先が指定されていません')
        if (self.subject is None or self.subject == ''):
            raise Exception('件名は必須です')
        if (self.text is None or self.text == ''):
            raise Exception('メール本文は必須です')
        
        params = { 
          'api_user': self.api_user,
          'api_key': self.api_key,
          'to': self.to_address,
          'from': self.from_address,
          'subject': self.subject,
          'text': self.text
        }
        
        if (self.html != ''):
            params.html = self.html;
        
        json_data = json.dumps(params).encode('utf-8')
        method = 'POST'
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        request = urllib.request.Request(self.url, data=json_data, method=method, headers=headers)
        try:
            with urllib.request.urlopen(request) as response:
                response_body = response.read().decode('utf-8')
            return json.dumps(response_body)
        except urllib.error.HTTPError as err:
            raise Exception(err.read())
