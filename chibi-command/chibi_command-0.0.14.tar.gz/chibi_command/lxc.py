from chibi.atlas import Chibi_atlas
from chibi_command import Command, Command_result
from chibi_hybrid.chibi_hybrid import Chibi_hybrid


class Info_result( Command_result ):
    def parse_result( self ):
        result = Chibi_atlas()
        for l in self.result.split( '\n' ):
            l = l.strip()
            if not l:
                continue
            k, v = l.split( ':' )
            v = v.strip()
            result[k.lower()] = v.lower()
        self.result = result

    @property
    def is_running( self ):
        return self.result.state == 'running'


class Create( Command ):
    command = 'lxc-create'
    captive = False

    @Chibi_hybrid
    def name( cls, name ):
        return cls( '-n', name )

    @name.instancemethod
    def name( self, name ):
        self.add_args( '-n', name )
        return self

    @Chibi_hybrid
    def template( cls, template ):
        return cls( '-t', template )

    @template.instancemethod
    def template( self, template ):
        self.add_args( '-t', template )
        return self


class Start( Command ):
    command = 'lxc-start'
    captive = False

    @Chibi_hybrid
    def name( cls, name ):
        return cls( '-n', name )

    @name.instancemethod
    def name( self, name ):
        self.add_args( '-n', name )
        return self

    @Chibi_hybrid
    def daemon( cls ):
        return cls( '-d' )

    @daemon.instancemethod
    def daemon( self ):
        self.add_args( '-d' )
        return self


class Attach( Command ):
    command = 'lxc-attach'
    captive = False

    @Chibi_hybrid
    def name( cls, name ):
        return cls( '-n', name )

    @name.instancemethod
    def name( self, name ):
        self.add_args( '-n', name )
        return self

    def build_tuple( self, *args, **kw ):
        return (
            self.command, *self.build_kw( **kw ), *self.args, '--', *args )


class Info( Command ):
    command = 'lxc-info'
    captive = True
    args = ( '-H', )
    result_class = Info_result

    @Chibi_hybrid
    def name( cls, name ):
        return cls( '-n', name )

    @name.instancemethod
    def name( self, name ):
        self.add_args( '-n', name )
        return self
