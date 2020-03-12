from .circuit import _definition_context_stack
from .t import Type


class Event:
    def __init__(self, value):
        if not isinstance(value, Type):
            raise TypeError("Expected magma value for event")
        self.value = value


class Posedge(Event):
    verilog_str = "posedge"


class Negedge(Event):
    verilog_str = "negedge"


def posedge(value):
    return Posedge(value)


def negedge(value):
    return Negedge(value)


class Display:
    def __init__(self, display_str, *args):
        self.display_str = display_str
        self.args = args
        self.events = []
        self.cond = None

    def when(self, event):
        """
        Allows chaining to set event for display, e.g.

            m.display("x=%d", x).when(m.posedge(io.CLK))\
                                .when(m.negedge(io.ASYNCRESET))

        """
        if not isinstance(event, (Type, Event)):
            raise TypeError("Expected magma value or event for when argument")
        self.events.append(event)

    def get_inline_verilog(self):
        format_args = {}
        for arg in self.args:
            format_args[f"_display_var_{id(arg)}"] = arg

        display_args = ", ".join(format_args.keys())
        if display_args:
            display_args = ", " + display_args

        if not self.events:
            event_str = "*"
        else:
            event_strs = []
            for event in self.events:
                value = event
                if isinstance(event, Event):
                    value = value.value
                var = f"_display_var_{id(value)}"
                format_args[var] = value
                if isinstance(event, Event):
                    var = f"{event.verilog_str} {var}"
                event_strs.append(var)
        event_str = ", ".join(event_strs)

        format_str = f"""\
always @({event_str}) begin
    $display(\"{self.display_str}\"{display_args});
end
"""
        return format_str, format_args, {}


def display(display_str, *args):
    context = _definition_context_stack.peek()
    disp = Display(display_str, args)
    context.add_display(disp)
    return disp
