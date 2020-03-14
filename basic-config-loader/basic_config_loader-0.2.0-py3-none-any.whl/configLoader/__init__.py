import os
import json

if __name__ == '__main__':
    print("This file is not to be run on its own.")
    raise SystemExit(1)

def readFile(path):
    '''
    Read a file given by path and return the parsed JSON. This method is intended to be used by loadConfig and not on its own, so it contains no error handling.
    '''
    file = open(path)
    rawText = file.read()
    file.close()
    return json.JSONDecoder().decode(rawText)

def loadConfig(path, default={}, fromHome=True, topSearchPath=None, fullSearchAlways=False):
    '''
    Load a JSON configuration from a file.
    
    :param path: the path to look for the file. It is recommended to provide the result of os.path.join() rather than a manually typed path because a certain OS which must not be named has different path conventions than everyone else.

    :param default: the configuration to return if loading from the filesystem fails.
    
    :param fromHome: if True, look from the current user's home directory. If False, look from the root directory.
    
    :param topSearchPath: if None, only look in the specified path for the file. Otherwise, a path should be provided. 'HOME' can be filled in as a shortcut for os.environ['HOME']. The exact behavior depends on fullSearchAlways.

    :param fullSearchAlways: if False, and the directory specified in path is empty, move up one folder, up to topSearchPath, until a config file is found, and use the first file found. If no file is found, use the default config. If True, start with the default configuration and apply any changes from topSearchPath to path in order.

    :return: the configuration if loading was successful, or the default configuration if loading failed.
    '''
    
    #Handle the fromHome parameter, creating realPath, the path that the user really wants us to load from.
    if fromHome:
        if path[0] == '/' or path[0] == '\\':
            realPath = path[1:]
        else: realPath = path
        realPath = os.path.join(os.environ['HOME'], realPath)
    else: realPath = os.path.abspath(path)
    
    #If the user only wants to check the specified path, build a list with just that path. Otherwise, build the list of paths to try loading from.
    paths = [realPath]
    if topSearchPath != None:
        if topSearchPath == 'HOME': topSearchPath = os.environ['HOME']
        #Make sure that by popping stuff off of realPath, we will eventually get to topSearchPath to avoid infinite loops. If we have a problem, throw an error.
        if os.path.commonpath([realPath, topSearchPath]) != topSearchPath: raise ValueError("topSearchPath must be a prefix of realPath")
        currentPath = realPath
        while os.path.dirname(currentPath) != topSearchPath:
            currentPath = os.path.join(os.path.dirname(os.path.dirname(currentPath)), os.path.basename(currentPath))
            paths.append(currentPath)

    #Read the path list in the order appropriate for the behavior that the user wants.
    if fullSearchAlways:
        result = default
        for currentPath in paths[::-1]:
            try: result.update(readFile(currentPath))
            except: pass
    else:
        result = default
        for currentPath in paths:
            try:
                result = readFile(currentPath)
                break
            except: pass
    return result

