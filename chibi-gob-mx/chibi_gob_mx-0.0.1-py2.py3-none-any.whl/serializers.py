from marshmallow import Schema, fields as f, pre_load, EXCLUDE


class Catalog( Schema ):
    id = f.String( data_key='_id', required=True )
    count = f.Integer( required=True )
    endpoint = f.String( required=True )
    origin_url = f.Url( data_key='url', required=True )
    fields = f.List(
        f.String, data_key='variables', required=False, missing=list )
    name = f.String( required=False )


    @pre_load( pass_many=True )
    def get_result( self, data, **kw ):
        self.many = True
        return data[ 'results' ]

    class Meta:
        unknown = EXCLUDE
