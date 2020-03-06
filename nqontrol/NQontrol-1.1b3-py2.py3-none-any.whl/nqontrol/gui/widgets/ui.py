"""NQontrol UI class"""
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

import nqontrol
from nqontrol.general import settings
from nqontrol.gui import controller, widgets
from nqontrol.gui.dependencies import app


class UI(widgets.NQWidget):
    """The UI master object from which all subuis branch off.

    Attributes
    ----------
    _uiDevice : :obj:`UIDevice`
        The top level UI component.

    """

    def __init__(self):
        print(f"Running NQontrol {nqontrol.__version__}")

    @property
    def layout(self):
        """Return the elements' structure to be passed to a Dash style layout, usually with html.Div() as a top level container. For additional information read the Dash documentation at https://dash.plot.ly/.

        Returns
        -------
        html.Div
            The html/dash layout.

        """
        header = [
            html.Div(
                children=[
                    # Device No. Picker
                    html.H1(
                        f"ADwin Device No. {settings.DEVICE_NUM}",
                        className="col-auto col-sm-7 col-lg-auto align-self-center",
                    ),
                    # Workload and timestamp
                    html.Div(
                        children=[f"Workload: {0} Timestamp {0}"],
                        id="work_time",
                        className="col-auto ml-sm-auto ml-md-auto ml-lg-auto align-self-center",
                    ),
                ],
                className="row justify-content-start align-items-center",
            ),
            html.Div(
                children=[
                    # Ramp target
                    html.Div(
                        children=[
                            html.Div(
                                children=[
                                    html.Div(
                                        children=["Ramp"],
                                        className="col-2 align-self-center",
                                    ),
                                    dcc.RadioItems(
                                        options=[{"label": "Off", "value": 0}]
                                        + [
                                            {"label": i, "value": i}
                                            for i in range(
                                                1, settings.NUMBER_OF_SERVOS + 1
                                            )
                                        ],
                                        value=controller.getCurrentRampLocation(),
                                        id="rampTarget",
                                        className="col-10",
                                        inputClassName="form-check-input",
                                        labelClassName="form-check form-check-inline",
                                    ),
                                ],
                                className="row",
                            )
                        ],
                        className="col-12 col-md-6",
                    ),
                    # Save filename
                    html.Div(
                        children=[
                            dcc.Input(
                                placeholder="Save as...",
                                className="form-control",
                                value=controller.getCurrentSaveName(),
                                id="save_name",
                            )
                        ],
                        className="col-6 col-md-2 col-lg-2 ml-lg-auto ml-xl-auto",
                    ),
                    # Save Button
                    html.Div(
                        children=[
                            html.Button(
                                "Save",
                                id="device_save_button",
                                className="btn btn-primary w-100",
                            )
                        ],
                        className="col-3 col-md-2 col-lg-auto pl-0",
                    ),
                    # Reboot Button
                    html.Div(
                        children=[
                            html.Button(
                                "Reboot",
                                id="device_reboot_button",
                                className="btn btn-primary w-100",
                            )
                        ],
                        className="col-3 col-md-2 col-lg-auto pl-0",
                    ),
                    # Error message output
                    dcc.Store(id="error"),
                    dcc.Store(id="save_out"),
                ],
                className="row justify-content-start align-items-center",
            ),
        ]
        servoDetails = [
            widgets.servo_section.ServoWidget(i).layout
            for i in range(1, settings.NUMBER_OF_SERVOS + 1)
        ]
        rest = [
            html.Div(
                children=[
                    # ServoDesign Plot
                    widgets.second_order_section.sosWidget.layout,
                    # The Monitoring part of the Servo
                    widgets.monitor_section.digitalOsciWidget.layout,
                ],
                className="row",
            )
        ]
        # In this case, no Dash html.Div is returned but the pure list of elements. All elements are rows and the main UI object has a Bootstrap ContainerFluid as its wrapping component
        return html.Div(
            children=header + servoDetails + rest, className="container-fluid"
        )

    def setCallbacks(self):
        """Initialize all callbacks for the given element."""

        self.__setDeviceCallbacks()

        for i in range(1, settings.NUMBER_OF_SERVOS + 1):
            widgets.servo_section.ServoWidget(i).setCallbacks()

        widgets.monitor_section.digitalOsciWidget.setCallbacks()
        widgets.second_order_section.sosWidget.setCallbacks()

    # Callbacks for the device control, e.g. timestamp and workload.
    def __setDeviceCallbacks(self):

        worktime = "work_time"
        app.callback(Output(worktime, "children"), [Input("update", "n_intervals")])(
            self._workTimeCallback
        )

        reboot = "device_reboot_button"
        app.callback(Output("error", "data"), [Input(reboot, "n_clicks")])(
            self._rebootCallback
        )

        ramp_servo_target = "rampTarget"
        app.callback(Output("rampInfo", "data"), [Input(ramp_servo_target, "value")])(
            self._rampCallback
        )

        saveTextArea = "save_name"
        saveButton = "device_save_button"
        app.callback(
            Output("save_out", "data"),
            [Input(saveButton, "n_clicks"), Input(saveTextArea, "n_submit")],
            [State(saveTextArea, "value")],
        )(self._saveCallback)

    # Callback for Save Button
    @staticmethod
    def _saveCallback(n_button, _submit, filename):
        return controller.callSave(n_button, filename)

    # Callback for the RAMP switch
    @staticmethod
    def _rampCallback(targetInput):
        return controller.callToggleRamp(targetInput)

    # Reboot button
    @staticmethod
    def _rebootCallback(clicks):
        return controller.callReboot(clicks)

    # Workload output
    @staticmethod
    def _workTimeCallback(_input_):
        return controller.callWorkloadTimestamp()
