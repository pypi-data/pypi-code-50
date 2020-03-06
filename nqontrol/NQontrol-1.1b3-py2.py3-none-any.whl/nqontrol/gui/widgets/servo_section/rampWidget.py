"""NQontrol UI: Ramp Widget. Part of the servo section. Contains sliders for frequency and amplitude."""
# -*- coding: utf-8 -*-
# pylint: disable=duplicate-code
# ----------------------------------------------------------------------------------------
# For documentation please read the comments. For information about Dash and Plotly go to:
#
# https://dash.plot.ly/
# ----------------------------------------------------------------------------------------

import dash_core_components as dcc
import dash_html_components as html
from dash import callback_context
from dash.dependencies import Input, Output

from nqontrol.general import helpers, settings
from nqontrol.gui import controller
from nqontrol.gui.dependencies import app
from nqontrol.gui.widgets import NQWidget


class RampWidget(NQWidget):
    """Ramp section. Part of the servo section. Contains sliders for frequency and amplitude.s"""

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
                # Ramp title and current ramp
                html.Summary(
                    children=[
                        html.H3("Ramp", className="col-auto mt-0"),
                        html.Span(
                            id=f"current_ramp_{self._servoNumber}", className="col-auto"
                        ),
                    ],
                    className="row justify-content-between align-items-center",
                    # style={
                    #     "background-color": "#4C78A8",
                    #     "border": ".5px solid #4C78A8",
                    #     "border-radius": "4.5px",
                    # }
                ),
                # Amplitude label and slider
                html.Div(
                    children=[
                        html.P("Amplitude (V)", className="col-12"),
                        dcc.Slider(
                            id=f"ramp_amp_slider_{self._servoNumber}",
                            min=0.1,
                            max=10,
                            step=0.05,
                            value=controller.getServoAmplitude(self._servoNumber),
                            marks={i: f"{i}" for i in range(1, 11, 1)},
                            className="col-10",
                            updatemode="drag",
                        ),
                    ],
                    className="row justify-content-center",
                ),
                # Frequency label and slider
                html.Div(
                    children=[
                        html.P("Frequency (Hz)", className="col-12"),
                        dcc.Slider(
                            id=f"ramp_freq_slider_{self._servoNumber}",
                            min=helpers.convertStepsize2Frequency(
                                settings.RAMP_MIN_STEPSIZE
                            ),
                            max=helpers.convertStepsize2Frequency(
                                settings.RAMP_MAX_STEPSIZE
                            ),
                            step=(
                                helpers.convertStepsize2Frequency(
                                    settings.RAMP_MAX_STEPSIZE
                                )
                                - helpers.convertStepsize2Frequency(
                                    settings.RAMP_MIN_STEPSIZE
                                )
                            )
                            / 254,
                            value=controller.getServoFrequency(self._servoNumber),
                            marks={
                                i: f"{i}"
                                for i in range(
                                    int(
                                        helpers.convertStepsize2Frequency(
                                            settings.RAMP_MIN_STEPSIZE
                                        )
                                    )
                                    - 1,
                                    int(
                                        helpers.convertStepsize2Frequency(
                                            settings.RAMP_MAX_STEPSIZE
                                        )
                                    )
                                    + 1,
                                    50,
                                )
                            },
                            className="col-10",
                            updatemode="drag",
                        ),
                    ],
                    className="row justify-content-center",
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
        ramp_freq_slider = f"ramp_freq_slider_{self._servoNumber}"
        ramp_amp_slider = f"ramp_amp_slider_{self._servoNumber}"

        amp_out = f"current_ramp_{self._servoNumber}"

        app.callback(
            Output(amp_out, "children"),
            [Input(ramp_amp_slider, "value"), Input(ramp_freq_slider, "value")],
        )(self._rampCallback)

    # Callback for the Ramp unit's amplitude slider
    def _rampCallback(self, amp, freq):
        ctxt = callback_context
        return controller.callRamp(amp, freq, ctxt, self._servoNumber)
