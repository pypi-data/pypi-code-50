import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from ..Model.Model import Model
import json
from flask import request


class LayoutBuilder:

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', dbc.themes.BOOTSTRAP]

    def __init__(self, data=None):
        self.app = dash.Dash(__name__, external_stylesheets=self.external_stylesheets)
        self.model = self.__loadData(data)
        self.app.layout = self.initVis()
        self.loadCallbacks()
        self.loadShutdown()

    def __loadData(self, datain=None):
        data = datain
        if data == None:
            data = json.load(open("../../static/data/cifar.json"))
        m = Model(data)
        m.buildModel()
        return m


    def getFigure(self,model, classIndex, epochIndex=None, dvalue=None):
        if epochIndex == None:
            epochIndex = model.epochCount() - 1

        if dvalue == None:
            dvalue = 1

        figure = {
            'data': model.epoch(epochIndex).getFrame(classIndex),
            'layout': {
                'title': 'Class Name: ' + model.epoch(epochIndex).classNames[classIndex],
                'barmode': 'stack',
                'xaxis': {
                    # 'range': [-max(model.epoch(epochIndex).histsBoundMax.maxRight, model.epoch(epochIndex).histsBoundMax.maxRight), max(model.epoch(epochIndex).histsBoundMax.maxRight, model.epoch(epochIndex).histsBoundMax.maxRight)],
                    'range': [- round(dvalue * model.maxRangeXAxis()), round(dvalue * model.maxRangeXAxis())],
                    'autorange': False
                },
                'transition': {
                    'duration': 300,
                    'easing': 'linear'
                },
                'updatemenus': [
                    dict(
                        type="buttons",
                        buttons=[dict(label="Play",
                                      method="animate",
                                      args=[None, {"frame": {"duration": 500},
                                                   "fromcurrent": True, "transition": {"duration": 300,
                                                                                       "easing": "linear"}}])
                                 ]),
                ]
            },
            'frames': model.modelFrames(classIndex)
        }
        return figure

    def initVis(self):
        w = 3
        startEpoch = 0
        return html.Div(
            [
                dbc.Row(html.Br()),
                dbc.Row(dbc.Col([html.H1(id='header', children='Cifar Model, Epochs Count : ' + str(
                    self.model.epochCount()) + ', Selected Epoch: ' + str(self.model.epochCount()),
                                         style={
                                             'textAlign': 'center'
                                         }
                                         )]), align="center"),
                dbc.Row(
                    [
                        dbc.Col(html.Div([html.Br(), dcc.Slider(
                            id='epoch-slider',
                            min=0,
                            max=self.model.epochCount() - 1,
                            value=self.model.epochCount() - 1,
                            marks={str(x): str(x + 1) for x in range(self.model.epochCount())},
                            step=None
                        )]))
                    ]
                ),
                dbc.Row(dbc.Col(
                    dcc.Dropdown(id='range',
                                 options=[
                                     {'label': '0.2X', 'value': '0.2'},
                                     {'label': '0.25X', 'value': '0.25'},
                                     {'label': '0.3X', 'value': '0.3'},
                                     {'label': '0.5X', 'value': '0.5'},
                                     {'label': 'X', 'value': '1'},
                                     {'label': '2X', 'value': '2'},
                                     {'label': '3X', 'value': '3'},
                                     {'label': '4X', 'value': '4'},
                                     {'label': '5X', 'value': '5'},
                                 ],
                                 value='1',
                                 searchable=False,
                                 clearable=False,
                                 style={
                                     'textAlign': 'center'
                                 }
                                 ), width={"size": 4, "offset": 4}
                )),
                dbc.Row(
                    [
                        dbc.Col(html.Div(dcc.Graph(id=self.model.lastEpoch().classNames[0], figure=self.getFigure(self.model, 0))),
                                width=w),
                        dbc.Col(html.Div(dcc.Graph(id=self.model.lastEpoch().classNames[1], figure=self.getFigure(self.model, 1))),
                                width=w),
                        dbc.Col(html.Div(dcc.Graph(id=self.model.lastEpoch().classNames[2], figure=self.getFigure(self.model, 2))),
                                width=w),
                        dbc.Col(html.Div(dcc.Graph(id=self.model.lastEpoch().classNames[3], figure=self.getFigure(self.model, 3))),
                                width=w)

                    ],
                    align="center",
                ),
                dbc.Row(
                    [
                        dbc.Col(html.Div(dcc.Graph(id=self.model.lastEpoch().classNames[4], figure=self.getFigure(self.model, 4))),
                                width=w),
                        dbc.Col(html.Div(dcc.Graph(id=self.model.lastEpoch().classNames[5], figure=self.getFigure(self.model, 5))),
                                width=w),
                        dbc.Col(html.Div(dcc.Graph(id=self.model.lastEpoch().classNames[6], figure=self.getFigure(self.model, 6))),
                                width=w),
                        dbc.Col(html.Div(dcc.Graph(id=self.model.lastEpoch().classNames[7], figure=self.getFigure(self.model, 7))),
                                width=w)
                    ],
                    align="center",
                ),
                dbc.Row(
                    [
                        dbc.Col(html.Div(dcc.Graph(id=self.model.lastEpoch().classNames[8], figure=self.getFigure(self.model, 8))),
                                width=w),
                        dbc.Col(html.Div(dcc.Graph(id=self.model.lastEpoch().classNames[9], figure=self.getFigure(self.model, 9))),
                                width=w)
                    ],
                    align="center",
                )
            ]
        )


    def loadCallbacks(self):
        @self.app.callback(Output('header', 'children'), [Input('epoch-slider', 'value')])
        def update_output_div(value):
            return 'Cifar Model, Epochs Count : ' + str(self.model.epochCount()) + ', Selected Epoch: ' + str(value + 1)


        @self.app.callback([Output(x, 'figure') for x in self.model.lastEpoch().classNames],
                      [Input('range', 'value'), Input('epoch-slider', 'value')])
        def update_output_div(dvalue, svalue):
            return [self.getFigure(self.model, i, svalue, float(dvalue)) for i in range(len(self.model.lastEpoch().classNames))]

    def run(self, debug):
        print("Stop Server: " + 'http://127.0.0.1:5000' + "/shutdown")
        self.app.run_server(debug=debug, port=5000)


    def loadShutdown(self):
        def shutdown_server():
            func = request.environ.get('werkzeug.server.shutdown')
            if func is None:
                raise RuntimeError('Not running with the Werkzeug Server')
            func()

        @self.app.server.route('/shutdown', methods=['GET'])
        def shutdown():
            shutdown_server()
            return 'Server shutting down...'