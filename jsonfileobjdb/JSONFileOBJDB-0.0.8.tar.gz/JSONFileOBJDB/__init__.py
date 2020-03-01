from pathlib import Path
import json
# https://docs.python.org/3/library/pathlib.html#correspondence-to-tools-in-the-os-module
# https://medium.com/@thucnc/how-to-publish-your-own-python-package-to-pypi-4318868210f9

class create:

    def __init__( self , options=None ):
        self.options = options
        self.self = None
        if "save_path" in options:
            self.posix_save_path = Path( options[ "save_path" ] )
            self.save_path_string = options[ "save_path" ]
            self.posix_save_path_base_directory = self.posix_save_path.parent
            self.save_path_base_directory_string = str( self.posix_save_path_base_directory )
            self.load_json_file()
        elif "posix_obj" in options:
            self.posix_save_path = options[ "save_path" ]
            self.save_path_string = str( options[ "save_path" ] )
            self.posix_save_path_base_directory = self.posix_save_path.parent
            self.save_path_base_directory_string = str( self.posix_save_path_base_directory )
            self.load_json_file()

    def load_json_file( self ):
        # Make Parent Directory if it Doesn't Exist
        self.posix_save_path_base_directory.mkdir( parents=True , exist_ok=True )
        # If save file doesn't already exist , create and save blank JSON structure
        if not self.posix_save_path.is_file():
            print( "Save File Doesn't Exist , Creating" )
            self.self = {}
            self.save()
        else:
            with open( self.save_path_string ) as json_file:
                self.self = json.load( json_file )

    def save( self ):
        with open( self.save_path_string , 'w' ) as json_file:
            json.dump( self.self , json_file , ensure_ascii=False )
