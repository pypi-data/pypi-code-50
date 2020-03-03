## Class Pytochnog
#
# A python tool to the Tochnog Professional geotechnical FEM analysis programme
#
class Pytochnog:

    ## Python object constructor
    #
    #
    def __init__( self ):

        ## Member variable model
        #
        #  This is member variable model is holding the model data
        #
        self.model = { 'init': [] , 'data': [] } ;

        ## Member variable realvalue
        #
        #  This is member variable realvalue holding a real value
        #
        self.realvalue = 0.0 ;

        ## Member variable integervalue
        #
        #  This is member variable integervalue holding an integer value
        #
        self.integervalue = 0 ;
        pass

    ## Function echo: implements the echo command
    #
    #  @param self   : the object instance
    #  @param status : the echo status
    #
    def echo( self , status ):
        pass
