from chibi.atlas import Chibi_atlas
from .logger import *  # noqa


__all__ = logger.__all__ + [ 'Configuration' ]


class Configuration( Chibi_atlas ):
    def __getitem__( self, name ):
        return super().__getitem__( name )

    def __setitem__( self, name, value ):
        return super().__setitem__( name, value )


configuration = Configuration()
