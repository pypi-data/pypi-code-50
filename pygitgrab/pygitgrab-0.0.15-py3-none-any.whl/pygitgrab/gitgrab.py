
import json
import requests


class Entry:
    
    def __init__(self, args ):
        self.__dict__.update(args)
        
    def __repr__(self):
        return f"Entry< path='{self.path}' type='{self.type}' size={self.size} url='{self.download_url}' >"
        

def _getheaders(auth):
    headers = {'User-Agent': 'pygg' if auth is None else auth[0] }
    return headers
        
        
def getfolder(url, auth=None ):    
      
    headers = _getheaders(auth)
    with requests.get(url,auth=auth,headers=headers) as r:
        
        if r.status_code != 200:
            raise Exception( "can not load data", url, r.headers )
        
        raw = r.content
        body = raw.decode()
        data = json.loads( body )
        
        all = {}
        
        for entry in data:
            if isinstance( entry, str ):                
                raise Exception( data, r.headers )
                
            e = Entry( entry )
            all[ e.path ] = e

        return all


def getfolders( repourl, auth=None ):
    
    all = {}
    entries = getfolder( repourl, auth=auth )
   
    for path, entry in entries.items():
        
        if entry.type == "dir":
            sub = getfolders( entry.url, auth=auth )
            all.update( sub )
        else:
            all[path] = entry
            
    return all
    

def download_file(url, dest, auth=None):
    try:        
        headers = _getheaders(auth)
        
        with requests.get(url,auth=auth,headers=headers) as r:
            
            if r.status_code != 200:
                raise Execption( "can not load data", url, r.headers )
            
            data = r.content
            
            with open( dest, "wb" ) as f:
                f.write( data )
                
                return True
    
    except Exception as ex:
        print("error: ", ex )
    
    return False


    

