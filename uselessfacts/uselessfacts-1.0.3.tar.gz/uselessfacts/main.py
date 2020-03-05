import requests
formats = ['html' , 'md' , 'txt' , 'json']
languages = ['en','de']

def random_fact(format=None,language=None):
  if(format == None) :
    format = 'json'
  if(not formats.__contains__(format)):
      raise Exception(f'Invaid format , should be one of {str(formats)}')
  else:
   if(language == None) :
      language = 'en'
   else:
      if(not languages.__contains__(language)):
        raise Exception(f'Invalid language , should be one of {str(languages)}')
      else:
        language = language
  try:
    r = requests.get('https://uselessfacts.jsph.pl/random.{}?language={}'.format(format,language))
    return {
      'status_code' : r.status_code,
      'response' : r.json() if format == 'json' else r.text
    }
  except Exception as error:
    raise error
def daily_fact(format=None,language=None):
  if(format == None) :
    format = 'json'
  if(not formats.__contains__(format)):
    raise Exception(f'Invaid format , should be one of {str(formats)}')
  else:
   if(language == None) :
      language = 'en'
   else:
      if(not languages.__contains__(language)):
        raise Exception(f'Invalid language , should be one of {str(languages)}')
      else:
        language = language
  try:
    r = requests.get('https://uselessfacts.jsph.pl/today.{}?language={}'.format(format,language))
    return {
      'status_code' : r.status_code,
      'response' : r.json() if format == 'json' else r.text
    }
  except Exception as error:
    raise error
def get_fact(id=None , format=None):
  if(id == None):
    raise Exception('You must provide an id')
  if(format == None) :
    format = 'json'
  if(not formats.__contains__(format)):
      raise Exception(f'Invaid format , should be one of {str(formats)}')
  try:
    r = requests.get('https://uselessfacts.jsph.pl/{}.{}'.format(id,format))
    return {
      'status_code' : r.status_code,
      'response' : r.json() if format == 'json' else r.text
    }
  except Exception as error:
    raise Exception('Fact not found fool')
print(get_fact('8b1f4d4d-193a-4ad0-ad19-ae8cfc17de12'))