
import configparser


class Pull:
    
    def __init__(self, **kwargs ):
        self.__dict__.update(kwargs)
        
    def __repr__(self):
        return f"Pull< repo='{self.repo}' tag='{self.tag}' root='{self.root}' alias='{self.alias}' pattern='{self.pattern}' dest='{self.dest}' >"


def read_pull_config( path ):
    
    config = configparser.ConfigParser()
    config.read( path )

    allpulls = {}

    for sec in config.sections():
        
        if "url" not in config[sec].keys():
            print( f"url missing for pull '{sec}', no sync" )
            continue

        tag = "master"
        if "tag" in config[sec].keys():
            tag = config[sec]["tag"]

        url = config[sec]["url"]
        props = config[sec].items()
        
        toput = allpulls.setdefault( sec, [] )
        
        added = 0
        for k,v in props:
            if k == "url":
                continue
            param = v.split(",")
            dest = ""
            if len(param)==2:
                dest = param[1].strip(" '\"")
                    
            added += 1
            
            pull = Pull( repo=url.strip(" '\""),
                         tag=tag.strip(" '\""),
                         root=sec,
                         alias=k,
                         pattern=param[0].strip(" '\""),
                         dest=dest )
            
            toput.append( pull )
            
        if added == 0:
            print( f"empty pull '{sec}' found, no sync" )
            del allpulls[sec] # remove empty pull
    
    return allpulls

