# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashRabix(Component):
    """A DashRabix component.
DashRabix displays a CWL workflow using Rabix SVG.
It takes a CWL in JSON format.

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks.
- cwlWorkflow (string; required): JSON string with CWL workflow to render.
- style (dict; optional): Object with style fields.
- showHeader (boolean; optional): Show the title and header."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, cwlWorkflow=Component.REQUIRED, style=Component.UNDEFINED, showHeader=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'cwlWorkflow', 'style', 'showHeader']
        self._type = 'DashRabix'
        self._namespace = 'dash_rabix'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'cwlWorkflow', 'style', 'showHeader']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['cwlWorkflow']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DashRabix, self).__init__(**args)
