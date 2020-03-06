"""NQontrol UI: AutoLock Widget"""
# -*- coding: utf-8 -*-
# pylint: disable=duplicate-code
# ----------------------------------------------------------------------------------------
# For documentation please read the comments. For information about Dash and Plotly go to:
#
# https://dash.plot.ly/
# ----------------------------------------------------------------------------------------
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from nqontrol.gui import controller
from nqontrol.gui.dependencies import app
from nqontrol.gui.widgets.nqWidget import NQWidget


class AutoLockWidget(NQWidget):
    """Widget for the autolock in the servo sections.
    """

    def __init__(self, servoNumber):
        self._servoNumber = servoNumber

    @property
    def layout(self):
        """Return the elements' structure to be passed to a Dash style layout, usually with html.Div() as a top level container. For additional information read the Dash documentation at https://dash.plot.ly/.

        Returns
        -------
        html.Div
            The html/dash layout.

        """
        return html.Details(
            children=[
                html.Summary(
                    children=[
                        html.H3("Autolock", className="col-6"),
                        html.P(
                            controller.getLockString(self._servoNumber),
                            id=f"lockFeedback_{self._servoNumber}",
                            className="col-6 text-right mt-0 mb-0 pt-0 pb-0",
                        ),
                    ],
                    className="row justify-content-between align-items-center",
                    # style={
                    #     "background-color": "#4C78A8",
                    #     "border": ".5px solid #4C78A8",
                    #     "border-radius": "4.5px",
                    # }
                ),
                html.Div(
                    children=[
                        html.P(
                            "Threshold (V)",
                            className="col-3",
                            id=f"lockThresholdInfo_{self._servoNumber}",
                        ),
                        html.Div(
                            children=[
                                dcc.Dropdown(
                                    options=[
                                        {"label": ">", "value": True},
                                        {"label": "<", "value": False},
                                    ],
                                    value=controller.getLockGreater(self._servoNumber),
                                    id=f"lockGreaterDropdown_{self._servoNumber}",
                                    className="w-100",
                                    clearable=False,
                                    persistence=True,
                                    searchable=False,
                                ),
                                dcc.Store(
                                    id=f"lockGreaterDropdownStore_{self._servoNumber}"
                                ),
                            ],
                            className="col-3 offset-3",
                        ),
                        html.Div(
                            children=[
                                dcc.Input(
                                    id=f"lockThresholdInput_{self._servoNumber}",
                                    className="form-control w-100",
                                    placeholder="-10 bis 10V",
                                    value=controller.getLockThreshold(
                                        self._servoNumber
                                    ),
                                ),
                                dcc.Store(
                                    id=f"lockThresholdInputStore_{self._servoNumber}"
                                ),
                            ],
                            className="col-3",
                        ),
                    ],
                    className="row p-0 justify-content-between align-items-center",
                ),
                html.Div(
                    children=[
                        html.P(
                            f"Search range {controller.getLockRange(self._servoNumber)} (V)",
                            className="col-5",
                            id=f"lockRangeSliderStore_{self._servoNumber}",
                        ),
                        html.Div(
                            children=[
                                dcc.RangeSlider(
                                    min=-10,
                                    max=10,
                                    id=f"lockRangeSlider_{self._servoNumber}",
                                    allowCross=False,
                                    persistence=True,
                                    step=0.1,
                                    value=controller.getLockRange(self._servoNumber),
                                    marks={-10: "-10", 0: "0", 10: "10"},
                                    className="w-100",
                                    updatemode="drag",
                                )
                            ],
                            className="col-7 mt-3 pt-1 pb-1",
                        ),
                    ],
                    className="row p-0 justify-content-between align-items-center",
                ),
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                dcc.Checklist(
                                    options=[{"label": "Relock", "value": "on"}],
                                    className="w-100 pl-0",
                                    inputClassName="form-check-input",
                                    labelClassName="form-check",
                                    id=f"lockRelockChecklist_{self._servoNumber}",
                                ),
                                dcc.Store(
                                    id=f"lockRelockChecklistStore_{self._servoNumber}"
                                ),
                            ],
                            className="col-3",
                        ),
                        html.Div(
                            children=[
                                html.Button(
                                    f"{controller.callLockButtonLabel(self._servoNumber)}",
                                    className="w-100 btn btn-primary",
                                    id=f"lockStateButton_{self._servoNumber}",
                                ),
                                dcc.Store(
                                    id=f"lockStateButtonStore_{self._servoNumber}"
                                ),
                            ],
                            className="col-3 ml-auto",
                        ),
                    ],
                    className="row p-0 pb-2 justify-content-between align-items-center",
                ),
            ],
            className="col-12 d-inline mt-1 mr-2",
            style={
                "background-color": "#f2f4f5",
                "border": ".5px solid #f2f4f5",
                "border-radius": "4.5px",
            },
        )

    def setCallbacks(self):
        """Initialize all callbacks for the given element."""

        # Feedback label updater
        app.callback(
            Output(f"lockFeedback_{self._servoNumber}", "children"),
            [Input(f"update", "n_intervals")],
        )(self._lockStringCallback)

        # Dropdown for autolock direction
        app.callback(
            Output(f"lockGreaterDropdownStore_{self._servoNumber}", "data"),
            [Input(f"lockGreaterDropdown_{self._servoNumber}", "value")],
        )(self._lockGreaterCallback)

        # Threshold input field
        app.callback(
            Output(f"lockThresholdInputStore_{self._servoNumber}", "data"),
            [Input(f"lockThresholdInput_{self._servoNumber}", "value")],
        )(self._lockThresholdCallback)

        # Threshold feedback label, takes the updated information out of the dcc.Store components mentioned in the above two callbacks
        app.callback(
            Output(f"lockThresholdInfo_{self._servoNumber}", "children"),
            [
                Input(f"lockThresholdInputStore_{self._servoNumber}", "data"),
                Input(f"lockGreaterDropdownStore_{self._servoNumber}", "data"),
            ],
            [
                State(f"lockThresholdInputStore_{self._servoNumber}", "data"),
                State(f"lockGreaterDropdownStore_{self._servoNumber}", "data"),
            ],
        )(self._lockThresholdInfoCallback)

        # Lock search range slider
        app.callback(
            Output(f"lockRangeSliderStore_{self._servoNumber}", "children"),
            [Input(f"lockRangeSlider_{self._servoNumber}", "value")],
        )(self._lockRangeCallback)

        # Callback of the trigger button
        app.callback(
            Output(f"lockStateButtonStore_{self._servoNumber}", "data"),
            [Input(f"lockStateButton_{self._servoNumber}", "n_clicks")],
        )(self._lockStateCallback)

        # Both button and change of ADwin internal state can change the label of the button
        app.callback(
            Output(f"lockStateButton_{self._servoNumber}", "children"),
            [
                Input(f"lockStateButtonStore_{self._servoNumber}", "data"),
                Input(f"lockFeedback_{self._servoNumber}", "children"),
            ],
        )(self._lockButtonLabelCallback)

        # Relock checkbox
        app.callback(
            Output(f"lockRelockChecklistStore_{self._servoNumber}", "data"),
            [Input(f"lockRelockChecklist_{self._servoNumber}", "value")],
        )(self._lockRelockCallback)

    #######################################################################################################
    # All callbacks need to return a function to be bound to that callback, defined below
    #######################################################################################################

    def _lockThresholdInfoCallback(self, _trigger1, _trigger2, threshold, greater):
        return controller.callLockThresholdInfo(threshold, greater, self._servoNumber)

    def _lockStateCallback(self, n_clicks):
        return controller.callLockState(n_clicks, self._servoNumber)

    def _lockButtonLabelCallback(self, _data, _children):
        return controller.callLockButtonLabel(self._servoNumber)

    def _lockRelockCallback(self, value):
        return controller.callLockRelock(value, self._servoNumber)

    def _lockThresholdCallback(self, threshold):
        return controller.callLockThreshold(threshold, self._servoNumber)

    def _lockGreaterCallback(self, greater):
        return controller.callLockGreater(greater, self._servoNumber)

    def _lockRangeCallback(self, lockRange):
        return controller.callLockRange(lockRange, self._servoNumber)

    def _lockStringCallback(self, _n_interval):
        return controller.getLockString(self._servoNumber)
