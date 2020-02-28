"""NQontrol UI class"""
# -*- coding: utf-8 -*-
# pylint: disable=unused-argument,too-many-lines

from abc import ABCMeta, abstractmethod

# ----------------------------------------------------------------------------------------
# Run file in cmd. App runs on http://127.0.0.1:8050/.
# Server adress is given in cmd window.
# For documentation please read the comments. For information about Dash and Plotly go to:
#
# https://dash.plot.ly/
# ----------------------------------------------------------------------------------------
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import nqontrol
from nqontrol import controller, general, settings
from nqontrol.dependencies import app

from . import controller, settings

# from dash_daq import ToggleSwitch


class UI:
    """The UI master object from which all subuis branch off.

    Attributes
    ----------
    _uiDevice : :obj:`UIDevice`
        The top level UI component.

    """

    def __init__(self):
        print(f"Running NQontrol {nqontrol.__version__}")
        self._uiDevice = UIDevice()

    @property
    def layout(self):
        """Return the app structure to be passed to a Dash style layout, usually with html.Div() as a top level container. For additional information read the Dash documentation at https://dash.plot.ly/.

        Returns
        -------
        html.Div
            The html/dash layout.

        """
        return html.Div(children=self._uiDevice.layout, className="container-fluid")

    def setCallbacks(self):
        """Initialize all callbacks for the given element."""
        self._uiDevice.setCallbacks()


class UIComponent:
    """Abstract class of UI components. In order to organize the Dash system and make features more modular, object structures are used for complex subsections of the interface. Callback functions and all user interaction to the backend are defined in the :obj:`controller` module. Callbacks are performed by the app (which is a Flask server that gets passed to gunicorn).
    Components also implement two default class functions/properties: `layout`, which returns the HTML layout in Dash syntax (sometimes, the layout has to be handled as part of initialization, when the layout needs more syntactic functionality), and `setCallbacks()``, which initializes all callbacks in startup. Dash usually requires the layout to be defined before the callbacks, as such, all calls to layout have to be made first. The `nqontrolUI` class starts a chain of calls to `setCallbacks()`, the majority of which are set in the `UIDevice` class.

    """

    __metaclass__ = ABCMeta

    @property
    @abstractmethod
    def layout(self):
        pass

    @abstractmethod
    def setCallbacks(self):
        pass


class UIDevice(UIComponent):
    """Main frame of the Interface. Implements a few top level elements of the UI, initializes and arranges all subsections.
    """

    def __init__(self):
        self.setUpComponents()

    def setUpComponents(self):
        """Set up UI components"""
        # Initiates all subcomponents in a special method and puts them into their respective lists for better readability.
        self._uiServoSection = []
        self._uiRamps = []
        self._uiAutoLocks = []
        for servoNumber in range(1, settings.NUMBER_OF_SERVOS + 1):
            self._uiServoSection.append(UIServoSection(servoNumber))
            self._uiRamps.append(UIRamp(servoNumber))
            self._uiAutoLocks.append(UIAutoLock(servoNumber))
        self._uiSDPlot = UIServoDesignPlot()
        self._monitor = UIMonitor()

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
                        "ADwin Device No. ",
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
            html.Details(
                children=[
                    html.Summary(
                        children=[
                            html.Span(
                                [controller.getServoName(i)],
                                id=f"servoName_{i}",
                                style={"width": "50%"},
                            )
                        ],
                        className="col-12 d-flex",
                    ),
                    # within the details component there needs to be another div wrapper for some reason. if removed, the servo and ramp sections will align as if on separate rows. Since bootstrap also requires the nesting of col- classes within row-classes, the structure looks a bit unreadable
                    html.Div(
                        children=[
                            html.Div(
                                children=[
                                    # Servo controls, including Input, Offset, Gain, Filters, Output
                                    self._uiServoSection[i - 1].layout,
                                    html.Div(
                                        children=[
                                            # Ramp sliders
                                            html.Div(
                                                [self._uiRamps[i - 1].layout],
                                                className="row m-0 p-0",
                                            ),
                                            html.Div(
                                                [self._uiAutoLocks[i - 1].layout],
                                                className="row m-0 p-0",
                                            ),
                                            html.Div(
                                                children=[
                                                    html.P(
                                                        "Name",
                                                        className="col-auto mb-0",
                                                    ),
                                                    html.Div(
                                                        children=[
                                                            dcc.Input(
                                                                id=f"servoNameInput_{i}",
                                                                className="form-control",
                                                            )
                                                        ],
                                                        className="col col-sm-4 col-md-2",
                                                    ),
                                                ],
                                                className="row m-0 pt-1 justify-content-end",
                                            ),
                                        ],
                                        className="col-12 col-xl-6 p-0",
                                    ),
                                ],
                                className="row",
                            )
                        ],
                        className="col-12",
                    ),
                ],
                className="row p-0",  # each html.Detail is a bootstrap row
                style={
                    "margin": ".1vh .5vh",
                    "border": ".5px solid #4C78A8",
                    "border-radius": "4.5px",
                },
            )
            for i in range(1, settings.NUMBER_OF_SERVOS + 1)
        ]  # List of html.Details, creating these one by one would be tedious
        rest = [
            html.Div(
                children=[
                    # ServoDesign Plot
                    self._uiSDPlot.layout,
                    # The Monitoring part of the Servo
                    self._monitor.layout,
                ],
                className="row",
            )
        ]
        # In this case, no Dash html.Div is returned but the pure list of elements. All elements are rows and the main UI object has a Bootstrap ContainerFluid as its wrapping component
        return header + servoDetails + rest

    def setCallbacks(self):
        """Initialize all callbacks for the given element."""
        for i in range(1, settings.NUMBER_OF_SERVOS + 1):
            # Pass along the servo number here since class has no specific servoNumber field
            # Technically these are callbacks of individual servo sections
            # Define the callback for the Servo Name input
            # servo name save file filename
            app.callback(
                Output(f"servoName_{i}", "children"),
                [Input(f"servoNameInput_{i}", "n_submit")],
                [State(f"servoNameInput_{i}", "value")],
            )(self.__createServoNameCallback(i))

        self.__setDeviceCallbacks()
        for componentList in (self._uiServoSection, self._uiRamps, self._uiAutoLocks):
            for unit in componentList:
                unit.setCallbacks()

        self._monitor.setCallbacks()
        self._uiSDPlot.setCallbacks()

    # Callbacks for the device control, e.g. timestamp and workload.
    def __setDeviceCallbacks(self):

        worktime = "work_time"
        app.callback(Output(worktime, "children"), [Input("update", "n_intervals")])(
            self.__createWorkTimeCallback(worktime)
        )

        reboot = "device_reboot_button"
        app.callback(Output("error", "data"), [Input(reboot, "n_clicks")])(
            self.__createRebootCallback(reboot)
        )

        ramp_servo_target = "rampTarget"
        app.callback(Output("rampInfo", "data"), [Input(ramp_servo_target, "value")])(
            self.__createRampCallback()
        )

        saveTextArea = "save_name"
        saveButton = "device_save_button"
        app.callback(
            Output("save_out", "data"),
            [Input(saveButton, "n_clicks"), Input(saveTextArea, "n_submit")],
            [State(saveTextArea, "value")],
        )(self.__createSaveCallback())

    # Callback for assigning a name to the individual servos
    @staticmethod
    def __createServoNameCallback(servoNumber):
        def callback(submit, name):
            return controller.callServoName(servoNumber, submit, name)

        return callback

    # Callback for Save Button
    @staticmethod
    def __createSaveCallback():
        def callback(n_button, submit, filename):
            return controller.callSave(n_button, filename)

        return callback

    # Callback for the RAMP switch
    @staticmethod
    def __createRampCallback():
        def callback(targetInput):
            return controller.callToggleRamp(targetInput)

        return callback

    # Reboot button
    @staticmethod
    def __createRebootCallback(inputElement):
        def callback(clicks):
            return controller.callReboot(clicks)

        return callback

    # Workload output
    @staticmethod
    def __createWorkTimeCallback(output):
        def callback(input_):
            return controller.callWorkloadTimestamp()

        return callback


class UIServoSection(UIComponent):
    """Servo Section"""

    def __init__(self, servoNumber):
        self._servoNumber = servoNumber

    def setCallbacks(self):
        """Initialize all callbacks for the given element."""

        # Offset callback
        offset = f"offset_{self._servoNumber}"
        sensitivityDropdown = f"input_sensitivity_dropdown_{self._servoNumber}"
        app.callback(
            Output(f"offset_label_{self._servoNumber}", "children"),
            [Input(offset, "n_submit"), Input(sensitivityDropdown, "value")],
            [State(offset, "value")],
        )(self.__createOffsetCallback())

        # Gain callback
        gain = f"gain_{self._servoNumber}"
        gainStore = f"gainStore_{self._servoNumber}"
        app.callback(
            Output(f"gain_label_{self._servoNumber}", "children"),
            [Input(gain, "n_submit"), Input("sosSwitchStorage", "data")],
            [State(gain, "value")],
        )(self.__createGainCallback())

        # Gain Store Callback
        app.callback(
            Output(gainStore, "data"),
            [Input(f"gain_label_{self._servoNumber}", "children")],
            [State(gain, "n_submit_timestamp")],
        )(self.__storeLastGainTimestamp())

        # Servo channels callback
        inputCheck = f"inputSectionCheck_{self._servoNumber}"
        filterCheck = f"filterSectionCheck_{self._servoNumber}"
        outputCheck = f"outputSectionCheck_{self._servoNumber}"

        app.callback(
            Output(f"channelChecklistStorage_{self._servoNumber}", "data"),
            [Input(inputCheck, "value"), Input(outputCheck, "value")],
        )(self.__createChannelCallback())

        app.callback(
            Output(f"filterChecklistStorage_{self._servoNumber}", "data"),
            [Input(filterCheck, "value")],
        )(self.__createFilterCallback())

        # Input sensitivity callback initialization
        # corresponding html ids
        label = f"input_sens_label_{self._servoNumber}"
        dropdown = f"input_sensitivity_dropdown_{self._servoNumber}"
        # callback definition
        app.callback(Output(label, "children"), [Input(dropdown, "value")])(
            self.__createInputSensitivityCallback()
        )

        # Aux sensitivity callback init
        # corresponding html ids
        label = f"aux_sens_label_{self._servoNumber}"
        dropdown = f"aux_sensitivity_dropdown_{self._servoNumber}"
        # callback definition
        app.callback(Output(label, "children"), [Input(dropdown, "value")])(
            self.__createAuxSensitivityCallback()
        )

    @property
    def layout(self):
        """Return the elements' structure to be passed to a Dash style layout, usually with html.Div() as a top level container. For additional information read the Dash documentation at https://dash.plot.ly/.

        Returns
        -------
        html.Div
            The html/dash layout.

        """
        return html.Div(
            children=[
                html.Div(
                    [
                        # Input Section
                        html.Div(
                            [
                                html.H3("Input", className="w-100 mt-0 pl-0"),
                                dcc.Checklist(
                                    options=[
                                        {"label": "Input", "value": "input"},
                                        {"label": "Offset", "value": "offset"},
                                    ],
                                    value=controller.getInputStates(self._servoNumber),
                                    id=f"inputSectionCheck_{self._servoNumber}",
                                    className="w-100 pl-0",
                                    inputClassName="form-check-input",
                                    labelClassName="form-check",
                                ),
                                html.P(
                                    "Input sensitivity (Limit: (V), Mode: )",
                                    className="w-100 mb-0",
                                    id=f"input_sens_label_{self._servoNumber}",
                                ),
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                dcc.Dropdown(
                                                    options=[
                                                        {"label": i, "value": i}
                                                        for i in range(4)
                                                    ],
                                                    value=controller.getInputSensitivity(
                                                        self._servoNumber
                                                    ),
                                                    clearable=False,
                                                    id=f"input_sensitivity_dropdown_{self._servoNumber}",
                                                )
                                            ],
                                            className="col-12 align-self-center",
                                        )
                                    ],
                                    className="row",
                                ),
                            ],
                            className="col-3",
                        ),
                        # Offset and Gain, also part of the input
                        html.Div(
                            children=[
                                html.P(
                                    "Offset", id=f"offset_label_{self._servoNumber}"
                                ),
                                dcc.Input(
                                    placeholder="-10 bis 10V",
                                    value=controller.getOffset(self._servoNumber),
                                    id=f"offset_{self._servoNumber}",
                                    className="form-control",
                                ),
                                # Gain
                                html.P("Gain", id=f"gain_label_{self._servoNumber}"),
                                dcc.Input(
                                    placeholder="Enter gain...",
                                    value=controller.getGain(self._servoNumber),
                                    id=f"gain_{self._servoNumber}",
                                    className="form-control",
                                ),
                                # Store component in order to determine how callGain was triggered. Saves previous timestamp
                                dcc.Store(id=f"gainStore_{self._servoNumber}"),
                                # Storage component to use as input channels checklist target in callbacks
                                dcc.Store(
                                    id=f"channelChecklistStorage_{self._servoNumber}"
                                ),
                            ],
                            className="col-3",
                        ),
                        # Filter section of the servo controls
                        html.Div(
                            children=[
                                html.H3("Filters", className="w-100 mt-0 pl-0"),
                                # Filter checklist
                                dcc.Checklist(
                                    options=controller.getFilterLabels(
                                        self._servoNumber
                                    ),
                                    value=controller.getActiveFilters(
                                        self._servoNumber
                                    ),
                                    id=f"filterSectionCheck_{self._servoNumber}",
                                    className="w-100",
                                    inputClassName="form-check-input",
                                    labelClassName="form-check",
                                ),
                                # Storage component to use as target for filter checklist target in callback
                                dcc.Store(
                                    id=f"filterChecklistStorage_{self._servoNumber}"
                                ),
                            ],
                            className="col-3",
                        ),
                        # Output section of the servo controls
                        html.Div(
                            [
                                html.H3("Output", className="w-100 mt-0 pl-0"),
                                # Channel Checklist for 'Aux' and 'Output'
                                dcc.Checklist(
                                    options=[
                                        {"label": "Aux", "value": "aux"},
                                        # {'label': 'Snap', 'value': 'snap'},
                                        {"label": "Output", "value": "output"},
                                    ],
                                    value=controller.getOutputStates(self._servoNumber),
                                    id=f"outputSectionCheck_{self._servoNumber}",
                                    className="w-100 pl-0",
                                    inputClassName="form-check-input",
                                    labelClassName="form-check",
                                ),
                                html.P(
                                    "Aux sensitivity (Limit: (V), Mode: )",
                                    className="w-100 mb-0",
                                    id=f"aux_sens_label_{self._servoNumber}",
                                ),
                                # The Aux sensitivity dropdown control
                                html.Div(
                                    # For some input components it helps to wrap them in an extra div and set that Div's properties instead, since the Dropdown will align with it. Therefore the nested row/col wrapper
                                    [
                                        html.Div(
                                            [
                                                dcc.Dropdown(
                                                    options=[
                                                        {"label": i, "value": i}
                                                        for i in range(4)
                                                    ],
                                                    value=controller.getAuxSensitivity(
                                                        self._servoNumber
                                                    ),
                                                    clearable=False,
                                                    id=f"aux_sensitivity_dropdown_{self._servoNumber}",
                                                )
                                            ],
                                            className="col-12 align-self-center",
                                        )
                                    ],
                                    className="row",
                                ),
                            ],
                            className="col-3",
                        ),
                    ],
                    className="row",
                )
            ],
            className="col-12 col-xl-6 d-inline",
        )

    # Callback for the Offset Input Field
    def __createOffsetCallback(self):
        def callback(n_submit, dropdownTrigger, inputValue):
            return controller.callOffset(self._servoNumber, inputValue)

        return callback

    # Callback for the Gain Input Field
    def __createGainCallback(self):
        def callback(n_submit, sosTrigger, inputValue):
            context = dash.callback_context
            return controller.callGain(context, self._servoNumber, inputValue)

        return callback

    @classmethod
    def __storeLastGainTimestamp(cls):
        def callback(input_, timestamp):
            return timestamp

        return callback

    # Callback for the input channels checklist
    def __createChannelCallback(self):
        def callback(inputValues, inputValues2):
            return controller.callServoChannels(
                self._servoNumber, inputValues + inputValues2
            )

        return callback

    def __createFilterCallback(self):
        def callback(value):
            return controller.callToggleServoFilters(self._servoNumber, value)

        return callback

    def __createAuxSensitivityCallback(self):
        def callback(selected):
            return controller.callAuxSensitivity(selected, self._servoNumber)

        return callback

    def __createInputSensitivityCallback(self):
        def callback(selected):
            return controller.callInputSensitivity(selected, self._servoNumber)

        return callback


class UIRamp(UIComponent):
    """Ramp section"""

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
                            min=general.convertStepsize2Frequency(
                                settings.RAMP_MIN_STEPSIZE
                            ),
                            max=general.convertStepsize2Frequency(
                                settings.RAMP_MAX_STEPSIZE
                            ),
                            step=(
                                general.convertStepsize2Frequency(
                                    settings.RAMP_MAX_STEPSIZE
                                )
                                - general.convertStepsize2Frequency(
                                    settings.RAMP_MIN_STEPSIZE
                                )
                            )
                            / 254,
                            value=controller.getServoFrequency(self._servoNumber),
                            marks={
                                i: f"{i}"
                                for i in range(
                                    int(
                                        general.convertStepsize2Frequency(
                                            settings.RAMP_MIN_STEPSIZE
                                        )
                                    )
                                    - 1,
                                    int(
                                        general.convertStepsize2Frequency(
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
            className="col-12 d-inline",
        )

    # Callback for the Ramp unit's amplitude slider
    def __createRampCallback(self):
        def callback(amp, freq):
            context = dash.callback_context
            return controller.callRamp(amp, freq, context, self._servoNumber)

        return callback

    def setCallbacks(self):
        """Initialize all callbacks for the given element."""
        ramp_freq_slider = f"ramp_freq_slider_{self._servoNumber}"
        ramp_amp_slider = f"ramp_amp_slider_{self._servoNumber}"

        amp_out = f"current_ramp_{self._servoNumber}"

        app.callback(
            Output(amp_out, "children"),
            [Input(ramp_amp_slider, "value"), Input(ramp_freq_slider, "value")],
        )(self.__createRampCallback())


class UIServoDesignPlot(UIComponent):
    """ServoDesign plotting section"""

    def __init__(self):
        self._uiSOSSection = UISecondOrderSection()

    @property
    def layout(self):
        return html.Div(
            children=[
                html.H2("Servo Design"),
                html.Div([self._uiSOSSection.layout], className="row"),
                html.Div(
                    children=[
                        html.Div(
                            [
                                "Plots the Second Order Section implemented by the Servo Design."
                            ],
                            className="col-12",
                        ),
                        html.Div(
                            children=[dcc.Graph(id="sdGraph", animate=False)],
                            className="col-12",
                        ),
                    ],
                    className="row",
                ),
            ],
            className="col-12 col-lg-6",
        )

    @staticmethod
    def _createGraphCallback():
        def callback(unplantTrigger, *args):
            return controller.callPlotServoDesign()

        return callback

    def setCallbacks(self):
        """Initialize all callbacks for the given element."""
        self._uiSOSSection.setCallbacks()

        graph = "sdGraph"
        uploadOutput = "uploadOutput"
        inputs = [Input(uploadOutput, "data")]

        for i in range(5):
            inputs.append(Input(f"filter_update_{i}", "data"))

        inputs.append(Input("sos_gain_label", "children"))

        app.callback(Output(graph, "figure"), inputs)(self._createGraphCallback())


class UISecondOrderSection(UIComponent):
    """Widget contains UI element for designing the filter section for servos. Contains 5 `UIFilter` widgets to assign different filters. Also containts an upload for a plant and displays a bode plot of the current filters.
    """

    def __init__(self):
        self._uiFilters = [
            UIFilter(filterIndex) for filterIndex in range(controller.getMaxFilters())
        ]

    @property
    def layout(self):
        """Return the elements' structure to be passed to a Dash style layout, usually with html.Div() as a top level container. For additional information read the Dash documentation at https://dash.plot.ly/.

        Returns
        -------
        html.Div
            The html/dash layout.

        """
        # Needing a content list beforehand
        childrenList = [
            html.Div(
                children=[
                    # Servo number target
                    html.Div(
                        children=[
                            dcc.Input(
                                type="number",
                                min=1,
                                max=settings.NUMBER_OF_SERVOS,
                                value=1,
                                persistence=True,
                                id="sos_servo",
                                className="form-control",
                            )
                        ],
                        className="col-3 col-sm-2 pr-0",
                    ),
                    # Upload field
                    html.Div(
                        [
                            dcc.Upload(
                                children=html.Div("Upload plant."),
                                id="plantUpload",
                                style={
                                    "height": "2.25rem",
                                    "line-height": "2.25rem",
                                    "borderWidth": "1px",
                                    "borderStyle": "dashed",
                                    "borderRadius": "5px",
                                    "textAlign": "center",
                                    "margin": "10px 0",
                                },
                                className="wl-100",
                            )
                        ],
                        className="col-9 col-sm-4",
                    ),
                    # Unplant button
                    html.Div(
                        [
                            html.Button(
                                "Unplant",
                                id="sosDelPlant",
                                className="btn btn-primary w-100",
                            )
                        ],
                        className="col-6 ml-sm-auto col-sm-2 col-lg-auto pl-sm-0",
                    ),
                    # Apply button
                    html.Div(
                        [
                            html.Button(
                                "Apply",
                                id="sos_apply",
                                className="btn btn-primary w-100",
                            )
                        ],
                        className="col-6 col-sm-2 col-lg-auto pl-sm-0",
                    ),
                    dcc.Store(id="sosSwitchStorage"),
                ],
                className="row align-items-center",
            ),
            html.Div(
                children=[
                    # Gain label
                    html.Div(["Gain"], id="sos_gain_label", className="col-3 col-sm-2"),
                    # Gain input field
                    html.Div(
                        [
                            dcc.Input(
                                placeholder="Enter gain...",
                                value=controller.getSDGain(),
                                id="sos_gain",
                                className="form-control w-100",
                            )
                        ],
                        className=" col-3 col-sm-4 pl-0 pl-sm-3",
                    ),
                    # Plant button timestamp storage to determine how controller.callPlantParse was triggered
                    dcc.Store(id="uploadOutput"),
                ],
                className="row align-items-center",
            ),
        ]
        for uiFilter in self._uiFilters:
            childrenList.append(uiFilter.layout)
        return html.Div(id="sos_unit", children=childrenList, className="col-12")

    @staticmethod
    def _createUploadCallback():
        def callback(filename, contents, n_clicks, timestamp, timestamp_old):
            return controller.callPlantParse(
                filename, contents, n_clicks, timestamp, timestamp_old
            )

        return callback

    @staticmethod
    def _createApplyServoCallback():
        def callback(n_clicks, servoNumber):
            return controller.callApplyServoDesign(servoNumber, n_clicks)

        return callback

    @staticmethod
    def _applyLabelCallback(servoNumber):
        def callback(value, applyNumber, n_clicks):
            return controller.callApplyFilterLabels(applyNumber, servoNumber, n_clicks)

        return callback

    @staticmethod
    def _applyValuesCallback(servoNumber):
        def callback(hiddenInput, applyNumber, n_clicks):
            return controller.callApplyFilterValues(applyNumber, servoNumber, n_clicks)

        return callback

    # Callback for the SOS Gain Input Field
    @staticmethod
    def __createSOSGainCallback():
        def callback(inputValue):
            return controller.callServoDesignGain(inputValue)

        return callback

    def setCallbacks(self):
        """Initialize all callbacks for the given element."""
        for filter_ in self._uiFilters:
            filter_.setCallbacks()

        for i in range(1, settings.NUMBER_OF_SERVOS + 1):
            sectionCheck = f"filterSectionCheck_{i}"

            # Apply the values
            app.callback(
                Output(sectionCheck, "value"),
                [Input("sosSwitchStorage", "data")],
                [State("sos_servo", "value"), State("sos_apply", "n_clicks")],
            )(self._applyValuesCallback(i))

            # Apply the labels
            app.callback(
                Output(sectionCheck, "options"),
                [Input(sectionCheck, "value")],
                [State("sos_servo", "value"), State("sos_apply", "n_clicks")],
            )(self._applyLabelCallback(i))

        delPlant = "sosDelPlant"
        plantUpload = "plantUpload"

        app.callback(
            Output("uploadOutput", "data"),
            [
                Input(plantUpload, "filename"),
                Input(plantUpload, "contents"),
                Input(delPlant, "n_clicks"),
            ],
            [State(delPlant, "n_clicks_timestamp"), State("uploadOutput", "data")],
        )(self._createUploadCallback())

        app.callback(
            Output("sosSwitchStorage", "data"),
            [Input("sos_apply", "n_clicks")],
            [State("sos_servo", "value")],
        )(self._createApplyServoCallback())

        # Gain callback
        gain = "sos_gain"
        app.callback(Output("sos_gain_label", "children"), [Input(gain, "value")])(
            self.__createSOSGainCallback()
        )


class UIFilter(UIComponent):
    """Widget for a single filter of the SecondOrderSection of the UI. Basically a row in the layout, containing inputs for filter type, main and secondary parameter.
    """

    def __init__(self, filterIndex):
        self._filterIndex = filterIndex

    @property
    def layout(self):
        """Return the elements' structure to be passed to a Dash style layout, usually with html.Div() as a top level container. For additional information read the Dash documentation at https://dash.plot.ly/.

        Returns
        -------
        html.Div
            The html/dash layout.

        """
        # Setting up dropdown options
        options = [{"label": "None", "value": None}]
        for filter_ in controller.getFilterOptions():
            options.append({"label": filter_.__name__, "value": filter_.__name__})
        return html.Div(
            children=[
                # Active checkbox
                html.Div(
                    [
                        dcc.Checklist(
                            id=f"filter_active_{self._filterIndex}",
                            options=[{"label": "", "value": self._filterIndex}],
                            value=controller.getFilterEnabled(self._filterIndex),
                            inputClassName="form-check-input",
                            labelClassName="form-check form-check-inline",
                        )
                    ],
                    className="col-2 col-sm-auto",
                ),
                # Dropdown filter type selection
                html.Div(
                    children=[
                        dcc.Dropdown(
                            options=options,
                            id=f"filter_unit_dropdown_{self._filterIndex}",
                            value=controller.getFilterDropdown(self._filterIndex),
                        )
                    ],
                    className="col-10 col-sm-3 col-lg-3",
                ),
                # Main filter parameter
                html.Div(
                    children=[
                        dcc.Input(
                            id=f"filter_frequency_input_{self._filterIndex}",
                            placeholder="fc",
                            className="form-control",
                            value=controller.getFilterMainPar(self._filterIndex),
                        )
                    ],
                    className="col-5 col-sm pl-sm-0 pr-0 pr-sm-3 ml-auto ml-sm-0",
                ),
                # Secondary filter parameter (optional)
                html.Div(
                    children=[
                        dcc.Input(
                            id=f"filter_optional_input_{self._filterIndex}",
                            placeholder="fcslope",
                            className="form-control",
                            value=controller.getFilterSecondPar(self._filterIndex),
                        )
                    ],
                    className="col-5 col-sm pl-0",
                ),
                # Description
                html.Div(
                    [controller.getFilterDescription(self._filterIndex)],
                    id=f"filter_description_{self._filterIndex}",
                    className="col-10 col-sm-5 col-lg-4 filter-font ml-auto ml-sm-0 pl-sm-0",
                ),
                dcc.Store(id=f"filter_update_{self._filterIndex}"),
            ],
            className="row justify-content-start align-items-center",
        )

    # Callback for visibility of filter input fields
    def _createFilterFieldCallback(self):
        def callback(  # pylint: disable=too-many-arguments
            dropdownInput,
            mainInput,
            secInput,
            servoTarget,
            plant,
            active,
            dropdown,
            main,
            sec,
            activeState,
        ):
            return controller.callFilterField(
                dropdown, main, sec, activeState, self._filterIndex
            )

        return callback

    def _createDescriptionCallback(self):
        def callback(dropdown, main, sec):
            return controller.callFilterDescription(
                dropdown, main, sec, self._filterIndex
            )

        return callback

    @classmethod
    def _createVisibilityCallback(cls):
        def callback(dropdownInput):
            return controller.callFilterVisible(dropdownInput)

        return callback

    def setCallbacks(self):
        """Initialize all callbacks for the given element."""

        dropdown = f"filter_unit_dropdown_{self._filterIndex}"
        mainInput = f"filter_frequency_input_{self._filterIndex}"
        secInput = f"filter_optional_input_{self._filterIndex}"
        description = f"filter_description_{self._filterIndex}"
        updateDiv = f"filter_update_{self._filterIndex}"
        servoTarget = f"sos_servo"
        activeCheck = f"filter_active_{self._filterIndex}"

        # Parameter/filter callback
        app.callback(
            Output(updateDiv, "data"),
            [
                Input(dropdown, "value"),
                Input(mainInput, "value"),
                Input(secInput, "value"),
                Input(servoTarget, "value"),
                Input("plantUpload", "filename"),
                Input(activeCheck, "value"),
            ],
            [
                State(dropdown, "value"),
                State(mainInput, "value"),
                State(secInput, "value"),
                State(activeCheck, "value"),
            ],
        )(self._createFilterFieldCallback())

        # Visibility callbacks
        for elem in [mainInput, secInput, description]:
            app.callback(Output(elem, "style"), [Input(dropdown, "value")])(
                self._createVisibilityCallback()
            )

        # Description callback
        app.callback(
            Output(description, "children"),
            [
                Input(dropdown, "value"),
                Input(mainInput, "value"),
                Input(secInput, "value"),
            ],
        )(self._createDescriptionCallback())


class UIMonitor(UIComponent):
    """This widget handles the display channels for the physical device. This is NOT the digital monitor graph, but a section below it, where the user can assign the ADwin hardware outputs to certain signals.
    """

    def __init__(self):
        self._layout = None
        self._sendChannels = (
            UIADwinMonitorChannels()
        )  # Init UI for physical monitor channels of ADwin device

    @property
    def layout(self):
        """Return the elements' structure to be passed to a Dash style layout, usually with html.Div() as a top level container. For additional information read the Dash documentation at https://dash.plot.ly/.

        Returns
        -------
        html.Div
            The html/dash layout.

        """
        self._layout = html.Div(
            # Monitoring Graph placeholder
            children=[
                # Monitor headline
                html.H2("Monitor"),
                # Servo target RadioItems
                html.Div(
                    children=[
                        html.Div("Servo", className="col-2 align-self-center"),
                        dcc.RadioItems(
                            options=[
                                {"label": i, "value": i}
                                for i in range(1, settings.NUMBER_OF_SERVOS + 1)
                            ],
                            value=1,
                            id="monitorTarget",
                            className="col-10",
                            persistence=True,
                            inputClassName="form-check-input",
                            labelClassName="form-check form-check-inline",
                        ),
                        dcc.Store(id="rampInfo"),
                    ],
                    className="row justify-content-start align-items-center",
                ),
                # Realtime graph
                html.Div(
                    children=[
                        html.Div(
                            children=[dcc.Graph(id="monitor_graph", animate=False)],
                            className="col-12 align-self-end",
                        )
                    ],
                    className="row",
                ),
                # Visible channels checklist
                html.Div(
                    children=[
                        html.Div(["Channels: "], className="col-auto d-inline"),
                        dcc.Checklist(
                            options=[
                                {"label": "Input", "value": "input"},
                                {"label": "Aux", "value": "aux"},
                                {"label": "Output", "value": "output"},
                            ],
                            persistence=True,
                            value=["input"],
                            inputClassName="form-check-input",
                            labelClassName="form-check form-check-inline",
                            id="monitor_check",
                        ),
                        # Callback output
                        dcc.Store(id="checklistTarget"),
                    ],
                    className="row justify-content-start align-items-center",
                ),
                # Update timer
                dcc.Interval(id="update", interval=1000, n_intervals=0),
                # Physical ADwin monitor channels
                self._sendChannels.layout,
            ],
            className="col-12 col-lg-6",
        )
        return self._layout

    def setCallbacks(self):
        """Initialize all callbacks for the given element."""

        # callbacks of the component which sets the ADwins internal monitoring Channels
        self._sendChannels.setCallbacks()

        # relevant HTML Ids
        servoInput = "monitorTarget"
        graph = "monitor_graph"
        checkList = "monitor_check"
        update = "update"

        app.callback(
            Output(graph, "figure"),
            [Input(update, "n_intervals"), Input(servoInput, "value")],
            [State(servoInput, "value"), State(checkList, "value")],
        )(self.__createMonitorCallback())

        app.callback(
            Output("checklistTarget", "data"),
            [Input(checkList, "value")],
            [State(servoInput, "value")],
        )(self.__createChannelCheckCallback())

    # Callback to the monitor
    @classmethod
    def __createMonitorCallback(cls):
        def callback(intervals, inputNum, servoNumber, checklistState):
            return controller.callMonitorUpdate(servoNumber, checklistState)

        return callback

    # Callback for checklist of visible monitor channels
    @classmethod
    def __createChannelCheckCallback(cls):
        def callback(visibleChannels, servoNumber):
            return controller.callMonitorUpdateChannels(servoNumber, visibleChannels)

        return callback


class UIADwinMonitorChannels(UIComponent):
    """Monitor section"""

    @property
    def layout(self):
        """Return the elements' structure to be passed to a Dash style layout, usually with html.Div() as a top level container. For additional information read the Dash documentation at https://dash.plot.ly/.

        Returns
        -------
        html.Div
            The html/dash layout.

        """
        self._layout = html.Details(  # pylint: disable=attribute-defined-outside-init
            children=[
                html.Summary(["ADwin Monitor Channels"], className="col-12"),
                html.P(
                    "Send a servo channel to one of the ADwin's physical monitor outputs.",
                    className="col",
                ),
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                # Channel index label
                                html.P(
                                    f"{i}", className="col-auto align-self-center m-0"
                                ),
                                # Servo target dropdown
                                html.Div(
                                    children=[
                                        dcc.Dropdown(
                                            options=[
                                                {"label": f"Servo {j}", "value": j}
                                                for j in range(
                                                    1, settings.NUMBER_OF_SERVOS + 1
                                                )
                                            ],
                                            value=controller.getMonitorsServo(i),
                                            placeholder="Servo channel",
                                            id=f"adwin_monitor_channel_target_{i}",
                                        )
                                    ],
                                    className="col",
                                ),
                                # Channel card dropdown
                                html.Div(
                                    children=[
                                        dcc.Dropdown(
                                            options=[
                                                {"label": "Input", "value": "input"},
                                                {"label": "Aux", "value": "aux"},
                                                {"label": "Output", "value": "output"},
                                                {"label": "TTL", "value": "ttl"},
                                            ],
                                            value=controller.getMonitorsCard(i),
                                            placeholder="Card",
                                            id=f"adwin_monitor_channel_card_{i}",
                                        )
                                    ],
                                    className="col",
                                ),
                                dcc.Store(id=f"store_adwin_monitor_channel_{i}"),
                            ],
                            className="row",
                        )
                        for i in range(1, settings.NUMBER_OF_MONITORS + 1)
                    ],
                    className="col-12",
                ),
            ],
            className="row p-0",  # The detail itself is a row
            style={
                "margin": ".1vh .5vh",
                "border": ".5px solid #4C78A8",
                "border-radius": "4.5px",
            },
        )
        return self._layout

    # The channel parameter is the monitor channel corresponding with the hardware channel on the device
    @staticmethod
    def __setADwinMonitorCallback(channel):
        # inp1 and inp2 are only used as triggers, servo and card refer to the servo that's being assigned to the channel and the monitoring data (input, output, aux, ttl)
        def callback(inp1, inp2, servo, card):
            return controller.callADwinMonitor(channel, servo, card)

        return callback

    def setCallbacks(self):
        """Initialize all callbacks for the given element."""

        for i in range(1, settings.NUMBER_OF_MONITORS + 1):
            # setting the function for each individual i
            # all HTML IDs relevant to the callback
            servoDropdown = f"adwin_monitor_channel_target_{i}"
            cardDropdown = f"adwin_monitor_channel_card_{i}"
            # stores the information, mainly Output dummy
            store = f"store_adwin_monitor_channel_{i}"
            # configuring the callback
            app.callback(
                Output(store, "data"),
                [Input(servoDropdown, "value"), Input(cardDropdown, "value")],
                [State(servoDropdown, "value"), State(cardDropdown, "value")],
            )(self.__setADwinMonitorCallback(i))


class UIAutoLock(UIComponent):
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
                    className="row p-0 justify-content-between align-items-center",
                ),
            ],
            className="col-12 d-inline mt-1",
        )

    def setCallbacks(self):
        """Initialize all callbacks for the given element."""
        app.callback(
            Output(f"lockFeedback_{self._servoNumber}", "children"),
            [Input(f"update", "n_intervals")],
        )(self.__createLockStringCallback())

        app.callback(
            Output(f"lockGreaterDropdownStore_{self._servoNumber}", "data"),
            [Input(f"lockGreaterDropdown_{self._servoNumber}", "value")],
        )(self.__createLockGreaterCallback())

        app.callback(
            Output(f"lockThresholdInputStore_{self._servoNumber}", "data"),
            [Input(f"lockThresholdInput_{self._servoNumber}", "value")],
        )(self.__createLockThresholdCallback())

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
        )(self.__createLockThresholdInfoCallback())

        app.callback(
            Output(f"lockRangeSliderStore_{self._servoNumber}", "children"),
            [Input(f"lockRangeSlider_{self._servoNumber}", "value")],
        )(self.__createLockRangeCallback())

        app.callback(
            Output(f"lockStateButtonStore_{self._servoNumber}", "data"),
            [Input(f"lockStateButton_{self._servoNumber}", "n_clicks")],
        )(self.__createLockStateCallback())

        app.callback(
            Output(f"lockStateButton_{self._servoNumber}", "children"),
            [
                Input(f"lockStateButtonStore_{self._servoNumber}", "data"),
                Input(f"lockFeedback_{self._servoNumber}", "children"),
            ],
        )(self.__createLockButtonLabelCallback())

        app.callback(
            Output(f"lockRelockChecklistStore_{self._servoNumber}", "data"),
            [Input(f"lockRelockChecklist_{self._servoNumber}", "value")],
        )(self.__createLockRelockCallback())

    def __createLockThresholdInfoCallback(self):
        def callback(trigger1, trigger2, threshold, greater):
            return controller.callLockThresholdInfo(
                threshold, greater, self._servoNumber
            )

        return callback

    def __createLockStateCallback(self):
        def callback(n_clicks):
            return controller.callLockState(n_clicks, self._servoNumber)

        return callback

    def __createLockButtonLabelCallback(self):
        def callback(data, children):
            return controller.callLockButtonLabel(self._servoNumber)

        return callback

    def __createLockRelockCallback(self):
        def callback(value):
            return controller.callLockRelock(value, self._servoNumber)

        return callback

    def __createLockThresholdCallback(self):
        def callback(threshold):
            return controller.callLockThreshold(threshold, self._servoNumber)

        return callback

    def __createLockGreaterCallback(self):
        def callback(greater):
            return controller.callLockGreater(greater, self._servoNumber)

        return callback

    def __createLockRangeCallback(self):
        def callback(lockRange):
            return controller.callLockRange(lockRange, self._servoNumber)

        return callback

    def __createLockStringCallback(self):
        def callback(n_interval):
            return controller.getLockString(self._servoNumber)

        return callback
