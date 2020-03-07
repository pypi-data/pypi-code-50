class SFRest(object):
  def __init__(self,  consumer_key, consumer_secret, redirect_uri, api_version=DEFAULT_API_VERSION):
     
    self.api_version = api_version
   
    self.consumer_key = consumer_key
    self.consumer_secret = consumer_secret
    self.redirect_uri = redirect_uri

    self.auth_uri = 'https://login.salesforce.com/services/oauth2/authorize'
    self.token_uri = 'https://login.salesforce.com/services/oauth2/token'


  def get_access_token_step1(self):
    response_type='code'
    url = '{}?response_type={}&display=popup&client_id={}&redirect_uri={}'.format(
            self.auth_uri, response_type, self.consumer_key, self.redirect_uri)
    return   requests.get(code_req).url


  def get_access_token_step2(self, code):
    body = {  'grant_type': 'authorization_code',
              'client_id': self.consumer_key,
              'client_secret': self.consumer_secret,
              'redirect_uri':  self.redirect_uri,
              'code': code
            }
    #print (body)
    return requests.post(self.token_uri, body).json()

  def set_access_info(self, access_token, instance_url):
    self.access_token = access_token
    self.instance_url = instance_url

  def describe_obj(self, obj='Account'):

    headers = {
      'Authorization': 'Bearer ' + self.access_token,
      'Content-Type': 'application/json;charset=UTF-8',
      'Accept': 'application/json'
    }
    
    #print ('headers: {}'. format(headers) )
    
    uri = '{}/services/data/{}/sobjects/{}/describe/'.format(self.instance_url, self.api_version, obj)
    print ('uri: ' + uri)
    response = requests.get(uri, headers=headers)
    return response
    
    # ------
  def wave(self, resource='dashboards'):
    headers = {
      'Authorization': 'Bearer ' + self.access_token,
      'Content-Type': 'application/json;charset=UTF-8',
      'Accept': 'application/json'
    }
  
    #print ('headers: {}'. format(headers) )
    
    uri = '{}/services/data/{}/wave/{}'.format(self.instance_url, self.api_version, resource)
    #print ('uri: ' + uri)
    response = requests.get(uri, headers=headers)
    return response

  def rest(self, resource=''):
    headers = {
      'Authorization': 'Bearer ' + self.access_token,
      'Content-Type': 'application/json;charset=UTF-8',
      'Accept': 'application/json'
    }
  
    #print ('headers: {}'. format(headers) )
    
    uri = '{}/services/data/{}{}'.format(self.instance_url, self.api_version, resource)
    #print ('uri: ' + uri)
    response = requests.get(uri, headers=headers)
    return response


  def run_query(self, soql=None):
    if not soql:
      raise RuntimeError("Must provide soql!")
    headers = {
      'Authorization': 'Bearer ' + self.access_token,
      'Content-Type': 'application/json;charset=UTF-8',
      'Accept': 'application/json'
    }
    
    #print ('headers: {}'. format(headers) )
    
    uri = '{}/services/data/{}/query?q={}'.format(self.instance_url, self.api_version, soql)
    #print ('uri: ' + uri)
    response = requests.get(uri, headers=headers)
    return response
x