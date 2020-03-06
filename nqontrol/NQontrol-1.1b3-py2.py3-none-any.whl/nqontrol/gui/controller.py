"""The main module handling interaction of an ADwin interface and a browser based Dash UI.
The main class handling the ADwin is :obj:`nqontrol.ServoDevice`.

Most init/loadFromSave functions start with `get`.

Most callback functions handling user interaction start with `call`.

"""
# pylint: disable=too-many-lines
import base64
import datetime
import logging as log

import plotly.graph_objs as go
from ADwin import ADwinError
from dash.exceptions import PreventUpdate
from fastnumbers import fast_real
from openqlab import io
from openqlab.analysis.servo_design import Filter
from plotly import subplots
from plotly.express import colors as clrs

from nqontrol.general import settings
from nqontrol.gui.dependencies import DEVICE

THEME = clrs.qualitative.T10
THEME2 = clrs.qualitative.G10

#
#
#
# INFORMATION GETTERS FOR UI - INIT / LOAD FUNCTIONS
# All methods that are fired on initial startup, initializing to default or loading from Save.
# These functions are not associated with a callback
#
#
#


def getCurrentSaveName():
    """Return name of save file as string if one has been specified.

    Concerns the header section of the UI.

    Returns
    -------
    :obj:`String`
        Name of the save file or empty string

    """
    if settings.SETTINGS_FILE is not None:
        return settings.SETTINGS_FILE
    return ""


def getServoName(servoNumber):
    """Return name attribute of servo: :obj:`servo.name` from Save or if specified in `settings.py`.

    Concerns the servo section of the UI.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`String`
        :obj:`servo.name`

    """
    if not isinstance(servoNumber, int):
        raise TypeError(f"servoNumber needs to be an integer, was {servoNumber}")
    if not servoNumber in range(1, settings.NUMBER_OF_SERVOS + 1):
        raise ValueError(
            f"servoNumber has to be in range 1 to (including) {settings.NUMBER_OF_SERVOS}."
        )
    servo = DEVICE.servo(servoNumber)
    return servo.name


def getMaxFilters():
    """Return the maximum number of filters for the :obj:`ServoDevice.servoDesign`.

    This is a used multiple times in the UI and not part of a specific component.

    Returns
    -------
    :obj:`int`
        Maximum number of filters for the associated :obj:`ServoDesign`.

    """
    servoDesign = DEVICE.servoDesign
    return servoDesign.MAX_FILTERS


def getCurrentRampLocation():
    """Return current channel of ADwin ramp from save. Default is None.

    Concerns the header section of the UI.


    Returns
    -------
    :obj:`int`
        Channel number of :obj:`servo` on which ramp is active.

    """
    return DEVICE.rampEnabled


def getInputStates(servoNumber):
    """Return a list of enabled input channels. Either from save or default (empty).

    Concerns the servo section of the UI.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`list`
        List containing names as strings.

    """
    if not isinstance(servoNumber, int):
        raise TypeError(f"servoNumber needs to be an integer, was {servoNumber}")
    if not servoNumber in range(1, settings.NUMBER_OF_SERVOS + 1):
        raise ValueError(
            f"servoNumber has to be in range 1 to (including) {settings.NUMBER_OF_SERVOS}."
        )
    checklist = []
    servo = DEVICE.servo(servoNumber)
    if servo.inputSw:
        checklist.append("input")
    if servo.offsetSw:
        checklist.append("offset")
    return checklist


def getOffset(servoNumber):
    """Return the servo's saved or default offset.

    Concerns the servo section of the UI.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`float`
        :obj:`servo.offset`

    """
    if not isinstance(servoNumber, int):
        raise TypeError(f"servoNumber needs to be an integer, was {servoNumber}")
    if not servoNumber in range(1, settings.NUMBER_OF_SERVOS + 1):
        raise ValueError(
            f"servoNumber has to be in range 1 to (including) {settings.NUMBER_OF_SERVOS}."
        )
    return DEVICE.servo(servoNumber).offset


def getGain(servoNumber):
    """Return servo's saved or default gain.

    Concerns the servo section of the UI.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`float`
        :obj:`servo.gain`

    """
    if not isinstance(servoNumber, int):
        raise TypeError(f"servoNumber needs to be an integer, was {servoNumber}")
    if not servoNumber in range(1, settings.NUMBER_OF_SERVOS + 1):
        raise ValueError(
            f"servoNumber has to be in range 1 to (including) {settings.NUMBER_OF_SERVOS}."
        )
    return DEVICE.servo(servoNumber).gain


def getActiveFilters(servoNumber):
    """Return list of active filters for filter-checklist.
    Load from save file or default empty list.
    The checklist is part of the servo section.
    Filter labels are loaded in :obj:`controller.getFilterLabels()`.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`list`
        List containing indices of active filters.

    """
    filters = DEVICE.servo(servoNumber).servoDesign.filters
    active = []
    for i, fil in enumerate(filters):
        if fil is not None and fil.enabled:
            active.append(i)
    return active


def getFilterLabels(servoNumber):
    """List containing filter-checklist labels (objects) as used by `Dash`.

    The checklist labels contain the short description of filters or default to `Filter {index}`.
    The checklist is part of the servo section.
    Filter states are loaded in :obj:`controller.getActiveFilters()`.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`list`
        List of labels.

    """
    labels = []
    servo = DEVICE.servo(servoNumber)
    servoDesign = servo.servoDesign
    for i in range(servoDesign.MAX_FILTERS):
        fil = servoDesign.get(i)
        if fil is not None:
            labels.append(fil.description)
        else:
            labels.append(f"Filter {i}")
    return [{"label": labels[i], "value": i} for i in range(servoDesign.MAX_FILTERS)]


def getFilterEnabled(filterIndex):
    """Load state of an individual filter.

    The UI in the second order section requires individual checkboxes, thus,
    filter states have to be loaded individually.

    Returns a list which is either empty or contains the filter index,
    signifying whether it is active or not (Checkbox UI elements work only with lists).
    The default state for a None filter however is active.
    So the only case in which the checkbox is set to inactive if an inactive filter is specified.

    This loads a state for the Second Order Section of the UI, not the servo sections!
    The getters for the servo section are :obj:`controller.getActiveFilters()`
    and :obj:`controller.getFiltersEnabled()`.

    Parameters
    ----------
    filterIndex : :obj:`int`
        filter index on :obj:`openqlab.analysis.servo_design.ServoDesign`

    Returns
    -------
    :obj:`list`
        List containing the filter index or empty list.

    """

    fil = DEVICE.servoDesign.get(filterIndex)
    if fil is not None:
        if not fil.enabled:
            return []
    return [filterIndex]


def getFilterDropdown(filterIndex):
    """Initialize the dropdown state of the filter UI for given index.
    If empty return None. Concerns the Second Order Section of the UI,
    not the servo's filter section!

    Parameters
    ----------
    filterIndex : :obj:`int`
        filter index on :obj:`openqlab.analysis.servo_design.ServoDesign`

    Returns
    -------
    :obj:`String`
        Name of the active filter class. None if inactive.

    """
    fil = DEVICE.servoDesign.get(filterIndex)
    if fil is not None:
        return fil.__class__.__name__
    return None


def getFilterMainPar(filterIndex):
    """Initialize the main parameter of the filter UI for given index.
    If no filter exists at given index return None.
    Concerns the Second Order Section of the UI.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`float`
        Parameter as a float or None.

    """
    fil = DEVICE.servoDesign.get(filterIndex)
    if fil is not None:
        return fil.corner_frequency
    return None


def getFilterSecondPar(filterIndex):
    """Initialize the second parameter of the filter UI for given index.
    If no filter exists at given index return None.
    Concerns the Second Order Section of the UI.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`float`
        Secondary parameter as float or None.

    """
    fil = DEVICE.servoDesign.get(filterIndex)
    if fil is not None:
        return fil.second_parameter
    return None


def getFilterDescription(filterIndex):
    """Initialize the description of the filter UI for given index.
    If no filter exists at given index return None.
    Concerns the Second Order Section of the UI.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`String`
        Filter description as a string or None.

    """
    fil = DEVICE.servoDesign.get(filterIndex)
    if fil is not None:
        return fil.description
    return None


def getOutputStates(servoNumber):
    """Return a list of enabled output channels. Either from save or default (empty).

    Concerns the servo section of the UI.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`list`
        List containing names as strings.
    """
    checklist = []
    servo = DEVICE.servo(servoNumber)
    if servo.auxSw:
        checklist.append("aux")
    # if servo.snapSw:
    #     checklist.append('snap')
    if servo.outputSw:
        checklist.append("output")
    return checklist


def getServoAmplitude(servoNumber):
    """Return the ramp amplitude setting for the specified :obj:`servo`.
    Load from save or default to `0.1`.

    Concerns the servo ramp section of the UI.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`float`
        Amplitude as float.

    """
    servo = DEVICE.servo(servoNumber)
    amplitude = servo.rampAmplitude
    return amplitude


def getServoFrequency(servoNumber):
    """Return the ramp frequency setting for specified :obj:`servo`.
    Load from save or defaukt to `20`.

    Concerns the servo ramp section of the UI.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    type
        Description of returned object.

    """
    servo = DEVICE.servo(servoNumber)
    frequency = servo.rampFrequency
    return frequency


def getInputSensitivity(servoNumber):
    """Return :obj:`servo.inputSensitivity`.
    Since each servo outputs 16 bit this basically relates to 'accuracy'.
    Please read the official docs for more information on how-to-use.

    Concerns the servo section of the UI.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`float`
        :obj:`servo.inputSensitivity`

    """
    servo = DEVICE.servo(servoNumber)
    return servo.inputSensitivity


def getAuxSensitivity(servoNumber):
    """Return :obj:`servo.auxSensitivity`.
    Since each servo outputs 16 bit this basically relates to 'accuracy'.
    Please read the official docs for more information on how-to-use.

    Concerns the servo section of the UI.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`float`
        :obj:`servo.auxSensitivity`

    """
    servo = DEVICE.servo(servoNumber)
    return servo.auxSensitivity


def getMonitorsServo(monitorNumber):
    """Return the target of a monitor channel.
    A servo channel can be assigned to one of {} monitor channels.

    Concerns the monitor section of the UI.
    Please note that this does not relate to the live graph of the UI
    but to the hardware monitor channels on the ADwin.

    Parameters
    ----------
    monitorNumber : :obj:`int`
        Monitor index.

    Returns
    -------
    :obj:`int`
        Monitor channel index or None.

    """.format(
        settings.NUMBER_OF_MONITORS
    )
    dev = DEVICE
    channelData = dev.monitors[monitorNumber - 1]
    # channel data is either a dict or None
    if channelData is not None:
        return channelData["servo"]
    return channelData


def getMonitorsCard(monitorNumber):
    """Return the card of a monitor channel.
    One of 'input', 'aux', 'output', 'ttl' or `None`.
    A servo channel can be assigned to one of {} monitor channels.

    Concerns the monitor section of the UI.
    Please note that this does not relate to the live graph of the UI
    but to the hardware monitor channels on the ADwin.

    Parameters
    ----------
    monitorNumber : :obj:`int`
        Monitor index.

    Returns
    -------
    :obj:`String`
        Card specifier or `None`.

    """.format(
        settings.NUMBER_OF_MONITORS
    )
    dev = DEVICE
    channelData = dev.monitors[monitorNumber - 1]
    if channelData is not None:
        return channelData["card"]
    return channelData


def getSDGain():
    """Return :obj:`ServoDevice.servoDesign.gain`,
    the gain of the :obj:`ServoDesign` associated with the device.

    Concerns the Second Order Section of the UI.

    Please note that functionality wise this equates to :obj:`servo.gain`
    if a :obj:`ServoDesign` is applied to a servo.
    The servo and ServoDesign then share a gain.
    The Second Order Section of the UI thus needs a separate input to prevent
    override to default when applying. Please read the documentation for further information.

    Parameters
    ----------

    Returns
    -------
    :obj:`float`
        Gain of the device's :obj:`ServoDesign` as a float.

    """
    servoDesign = DEVICE.servoDesign
    return servoDesign.gain


def getLockRange(servo):
    """Returns a list containing minimum and maximum value of the autolock sections RangeSlider.abs

    The AutoLock options are located in the servo section.

    Parameters
    ----------
    servo : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    obj:`list`
        [min, max]

    """
    servo = DEVICE.servo(servo)
    return [servo.lockSearchMin, servo.lockSearchMax]


def getLockThreshold(servo):
    """Returns the threshold value of the autolock.

    The AutoLock options are located in the servo section.

    Parameters
    ----------
    servo : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    obj:`float`
        The voltage value.

    """
    servo = DEVICE.servo(servo)
    return servo.lockThreshold


def getLockGreater(servo):
    """Return the initial value of the lock condition of a servo.
    The boolean translates to greater (True) or lesser than (False) the threshold.
    Part of the servo section.

    Parameters
    ----------
    servo : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`bool`
        The lock condition as a boolean.

    """
    servo = DEVICE.servo(servo)
    return servo.lockGreater


def getLockRelock(servo):
    """Return whether auto-relock is on or off for a given servo.

    Parameters
    ----------
    servo : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`list`
        Empty list means `False`, element in list means `True`.

    """
    result = []
    if DEVICE.servo(servo).relock:
        result.append("on")
    return result


def getLockString(servo):
    """Return a string description of the autolock state. This will be updated on a by-second interval. Contains information for the GUI on search state, relock and locked state.

    Parameters
    ----------
    servo : :obj:`int`
        The servo index.

    Returns
    -------
    :obj:`String`
        The description string.

    Raises
    ------
    TypeError
        `servo` needs to be an integer.
    ValueError
        `servo` has to be in the correct range fom 1 to the max number of servos (depends on your settings).
    """
    if not isinstance(servo, int):
        raise TypeError(f"servo parameter needs to be an integer, was {servo}")
    if not servo in range(1, settings.NUMBER_OF_SERVOS + 1):
        raise ValueError(
            f"servoNumber has to be in range 1 to (including) {settings.NUMBER_OF_SERVOS}."
        )
    servo = DEVICE.servo(servo)
    lockstatus = servo.lockSearch
    locked = servo.locked
    relock = servo.relock
    return f"search {int(lockstatus)} relock {int(relock)} locked {int(locked)}"


#
#
#
# INTERFACE FUNCTIONALITY
# These methods handle communication of device and interface.
# They are associated with callbacks.
#
#
#


def callServoName(servoNumber, submit, name):
    """Apply the name specified in the servo section's name input
    to the targeted :obj:`servo.name` and return the name string to update the UI.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`
    submit : :obj:`int`
        Number of times the input's submit event occured (pressing Enter while in input).
        None on startup.
    name : :obj:`String`
        Name for the :obj:`servo` and the UI's servo section.

    Returns
    -------
    :obj:`String`
        :obj:`servo.name`
    """
    if submit is None:
        raise PreventUpdate()
    servo = DEVICE.servo(servoNumber)
    servo.name = name
    return servo.name


def callInputSensitivity(selected, servoNumber):
    """Apply the input sensitivity as specified by the dropdown
    of the servo section's input options to :obj:`servo.inputSensitivity`
    and return information as a string to update UI.

    Parameters
    ----------
    selected : :obj:`int`
        One of the dropdown options. The mode is specified with ints from `0` to `3`.
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`String`
        Information formatted for the `html.P()` above the dropdown.
    """
    servo = DEVICE.servo(servoNumber)
    servo.inputSensitivity = selected
    limits = [10, 5, 2.5, 1.25]
    return f"Input sensitivity (Limit: {limits[selected]} V, Mode: {selected})"


def callAuxSensitivity(selected, servoNumber):
    """Apply the aux sensitivity as specified by the dropdown
    of the servo section's output options to :obj:`servo.auxSensitivity`
    and return information as a string to update UI.

    Parameters
    ----------
    selected : :obj:`String`
        One of the dropdown options. The mode is specified with ints from `0` to `3`.
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`String`
        Information formatted for the `html.P()` above the dropdown.

    """
    servo = DEVICE.servo(servoNumber)
    servo.auxSensitivity = selected
    limits = [10, 5, 2.5, 1.25]
    return f"Aux sensitivity (Limit: {limits[selected]} V, Mode: {selected})"


def callReboot(clicks):
    """Reboot the ADwin device.

    Return a :obj:`String` with information on reboot.
    Return `None` if button hasn't been pressed
    (to accound for Dash callbacks firing on start-up).

    Parameters
    ----------
    clicks : :obj:`int`
        Description of parameter `clicks`.

    Returns
    -------
    :obj:`String`
        Information on the reboot process for the UI.

    """
    if clicks is not None:
        try:
            dev = DEVICE
            dev.reboot()
            return "Rebooted successfully."
        except ADwinError:
            return "Reboot encountered an error."
    else:
        return None


def callSave(clicks, filename):
    """Save the :obj:`nqontrol.ServoDevice` to the
    "./src"-directory using the filename provided.

    If no filename was provided saves a 'untitled_device'.

    Parameters
    ----------
    clicks : :obj:`int`
        Description of parameter `clicks`.
    filename : :obj:`String`
        Specify a `String` as the potential filename. If not provided, save to 'untitled_device'.

    Returns
    -------
    :obj:`String`
        Text info on save process.

    """
    if (clicks is not None) and (clicks > 0):
        try:
            if filename is None:
                filename = "untitled_device"
            dev = DEVICE
            dev.saveDeviceToJson(filename)
            log.info(f"Saved device as JSON in: {filename}")
            return f"Saved as {filename}."
        except Exception as e:
            log.warning(e)
            raise PreventUpdate()
    else:
        raise PreventUpdate()


def callMonitorUpdate(servoNumber, visibleChannels):
    """Handle live plotting functionality for the UI.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`
    visibleChannels : :obj:`list`
        List of Strings specifying the signals to be shown, arbitrary choice of:
        ['input', 'aux', 'output'].

    Returns
    -------
    :obj:`plotly.graph_objs`
        Returns a plotly/Dash graph_object/figure, consisting of data and layout.
        See https://plot.ly/ for detailed info.

    """
    # a device has to be connected and only returns an updating figure
    # if channels are set to active via the Checklist element below the Graph UI
    if visibleChannels:
        servo = DEVICE.servo(servoNumber)
        # this should never happen anyway
        # if servo.fifoStepsize is None:
        #     servo.fifoStepsize = 10

        # Setting visible channels
        servo.realtime["ydata"] = visibleChannels
        # Would be a list containing at least one of the keywords used in `colors` below
        df = servo.takeData()
        # this will be a list of plotly.graph_objs
        traces = []
        # Assigning colors for specific channel tags, if not set manually,
        # colors are assigned by plotly but incosistently, depending on order of adding plots.
        colors = {"input": THEME[0], "aux": THEME[1], "output": THEME[2]}
        for label in visibleChannels:
            data = df[label]
            # For more options on styling the graphs, please look at the plotly documentation
            traces.append(
                go.Scattergl(
                    x=df.index,
                    y=data,
                    name=label,
                    mode="lines",
                    marker=dict(color=colors[label]),
                )
            )
        figure = {
            "data": traces,
            "layout": go.Layout(yaxis=dict(title="Amplitude (V)", uirevision="foo")),
        }
        return figure
    raise PreventUpdate()


def callMonitorUpdateChannels(servoNumber, visibleChannels):
    """Set visible channels attribute of :obj:`servo.realtime`.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`
    visibleChannels : :obj:`list`
        List of Strings specifying the signals to be shown, arbitrary choice of:
        ['input', 'aux', 'output'].

    Returns
    -------
    :obj:`String`
        Feedback string on what was applied. Just for UI purposes.

    """
    if visibleChannels:
        servo = DEVICE.servo(servoNumber)
        servo.realtime["ydata"] = visibleChannels
        return "ydata set to" + str(visibleChannels)
    return "Empty channels"


def callWorkloadTimestamp():
    """Handle callback for Workload and Timestamp output in the UIs header section.

    Parameters
    ----------

    Returns
    -------
    :obj:`String`
        The workload and timestamp in a String description.

    """
    try:
        return f"Workload: {DEVICE.workload} Timestamp: {DEVICE.timestamp}"
    except ADwinError:
        return "Workload: ERR Timestamp: ERR"


def callOffset(servoNumber, offset):
    """Handle the servo offset input callback for the UI's servo input section.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`
    offset : :obj:`String`
        String from the input field.

    Returns
    -------
    :obj:`String`
        The offset embedded in a string for the html.P label.

    """
    servo = DEVICE.servo(servoNumber)
    try:
        offset = fast_real(offset, raise_on_invalid=True)
    except (ValueError, TypeError):
        raise PreventUpdate("Empty or no real number input.")
    # Please note that servo checks for correct value.
    servo.offset = offset
    return f"Offset ({servo.offset:.2f} V)"


def callGain(context, servoNumber, gain):
    """Handle the servo gain input callback for the UI's servo input section.

    Parameters
    ----------
    context : :obj:'json'
        Dash callback context. Please check the dash docs for more info.
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`
    gain : :obj: `String`
        String from the input field.

    Returns
    -------
    :obj:`String`
        The gain embedded in a string for the html.P label.

    """
    servo = DEVICE.servo(servoNumber)

    # determining context of input
    triggered = context.triggered[0]["prop_id"].split(".")[0]

    if "gain" in triggered:
        # case when gain is changed by submitting the input with Enter
        try:
            gain = fast_real(gain, raise_on_invalid=True)
        except (ValueError, TypeError):
            raise PreventUpdate("Empty or no real number input.")
        if servo.gain != gain:
            servo.gain = gain

    return f"Gain ({servo.gain:.2f})"


def callServoDesignGain(gain):
    """Handle the dummy ServoDesign gain callback for the UI.
    The :obj:`ServoDesign` is associated with the :obj:`nqontrol.ServoDevice`
    and can then be applied to a :obj:`servo`.

    Parameters
    ----------
    gain: :obj:`String`
        String from the input field.

    Returns
    -------
    :obj:`String`
        The gain embedded in a string for the html.P label.

    """
    try:
        gain = fast_real(gain, raise_on_invalid=True)
    except (ValueError, TypeError):
        raise PreventUpdate("Empty or no real number input.")
    # The
    servoDesign = DEVICE.servoDesign
    if servoDesign.gain != gain:
        servoDesign.gain = gain
    return "Gain (" + str(servoDesign.gain) + ")"


def callServoChannels(servoNumber, inputValues):
    """Handle the checklists for both the input and output section of servo controls.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`
    inputValues : :obj:`list`
        List for either input or output section.
        Labels for input section are 'input', 'offset'.
        For output section 'aux' and 'output'.

    Returns
    -------
    type
        Description of returned object.

    """
    servo = DEVICE.servo(servoNumber)
    if "input" in inputValues:
        servo.inputSw = True
    else:
        servo.inputSw = False

    if "offset" in inputValues:
        servo.offsetSw = True
    else:
        servo.offsetSw = False

    if "aux" in inputValues:
        servo.auxSw = True
    else:
        servo.auxSw = False

    # if 'snap' in inputValues:
    #     servo.snapSw = True
    # else:
    #     servo.snapSw = False

    if "output" in inputValues:
        servo.outputSw = True
    else:
        servo.outputSw = False

    return ""


def callApplyServoDesign(servoNumber, n_clicks):
    """Callback for the 'Apply'-Button in the Second Order Section of the UI.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`
    n_clicks : :obj:`int`
        Integer indicating times the Button has been clicked.
        Used to prevent callback from firing on start-up.

    Returns
    -------
    :obj:`String`
        String description to pass on to UI label.

    """
    if n_clicks is not None:
        servoDesign = DEVICE.servoDesign
        servo = DEVICE.servo(servoNumber)
        servo.applyServoDesign(servoDesign)
        return f"Applied ServoDesign on {servoNumber}."
    raise PreventUpdate()


def callApplyFilterLabels(applyNumber, servoNumber, n_clicks):
    """Handle updating filter labels in the servo control section
    when 'Apply' button is pressed for the Second Order Section.

    Due to the callback mechanic, an additional parameter `applyNumber` has to be passed,
    to ensure the labels are only updated in the corresponding section.

    Parameters
    ----------
    applyNumber : :obj:`int`
        Parameter compared to the `servoNumber`.
        Only fires if they are the same.
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`
    n_clicks : :obj:`int`
        Indicates times the button has been clicked.
        Used to prevent callback execution on start-up.

    Returns
    -------
    :obj:`list`
        List containing the new labels of the checklist UI element.
        Each label is defined as {`label`: xxx, `value`: xxx}.
        The value will always correspond to the filter index.

    """
    if (applyNumber == servoNumber) and (n_clicks is not None):
        servoDesign = DEVICE.servoDesign
        labels = []
        for i in range(servoDesign.MAX_FILTERS):
            fil = servoDesign.get(i)
            if fil is not None:
                labels.append(fil.description)
            else:
                labels.append(f"Filter {i}")
        return [
            {"label": labels[i], "value": i} for i in range(servoDesign.MAX_FILTERS)
        ]
    raise PreventUpdate()


def callApplyFilterValues(applyNumber, servoNumber, n_clicks):
    """Handle updating filter checklist values in the servo control section
    when 'Apply' button is pressed for the Second Order Section.

    Due to the callback mechanic, an additional parameter `applyNumber` has to be passed,
    to ensure the checklist values are only updated in the corresponding section.

    Parameters
    ----------
    applyNumber : :obj:`int`
        Parameter compared to the `servoNumber`. Only fires if they are the same.
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`
    n_clicks : :obj:`int`
        Indicates times the button has been clicked. Used to prevent callback execution on start-up.

    Returns
    -------
    :obj:`list`
        List containing the values of all active filters for checklist UI element.
        The value corresponding to each filter is its respective index.

    """
    if (applyNumber == servoNumber) and (n_clicks is not None):
        servoDesign = DEVICE.servoDesign
        values = []
        for i in range(servoDesign.MAX_FILTERS):
            fil = servoDesign.get(i)
            if fil is not None and fil.enabled:
                values.append(i)
        return values
    raise PreventUpdate()


def callToggleServoFilters(servoNumber, values):
    """Handle callback of the filter checklist in the servo section of the UI.
    Passes a list of active filters to the :obj:`servo`.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`
    values : :obj:`list`
        List containing the indices of active filters.

    Returns
    -------
    :obj:`String`
        Just an empty string since UI callback needs an output.

    """
    servoDesign = DEVICE.servo(servoNumber).servoDesign
    changed = False
    for i in range(servoDesign.MAX_FILTERS):
        f = servoDesign.get(i)
        if f is not None:
            if i in values:
                f.enabled = True
            else:
                f.enabled = False
            changed = True
    if changed:
        DEVICE.servo(servoNumber).applyServoDesign()
    return ""


def callPlantParse(  # pylint: disable=unused-argument
    filename, contents, n_clicks, timestamp, timestamp_old
):
    """Handle parsing of uploaded plant for :obj:`ServoDesign` of the Second Order Section.
    Also handles 'unplanting'.
    Has to be handled by one function as both callbacks would target the same output container.

    Parameters
    ----------
    filename : :obj:`String`
        Name of the input file. Dash does not send the full path.
    contents : :obj:`String`
        Base64 encoded string of the file contents.
    n_clicks : :obj:`int`
        Number of times the 'Unplant' button has been clicked

    Returns
    -------
    :obj:`String`
        Timestamp of the last time the button was clicked.

    """
    if n_clicks is None and contents is None:
        raise PreventUpdate()
    servoDesign = DEVICE.servoDesign
    # first check if the callback has been fired by the unplant button
    if timestamp_old != timestamp:
        servoDesign.plant = None
    elif contents is not None:
        _, content_string = contents.split(",")
        decoded = base64.b64decode(content_string).decode("utf-8", "ignore")
        try:
            df = io.reads(decoded)
            servoDesign.plant = df
        except Exception as e:
            log.warning(e)
            raise PreventUpdate(str(e))
    return timestamp


def callPlotServoDesign():
    """Handle plotting of amplitude and phase of the ServoDesign
    associated with the device over frequency.
    Part of the UI's Second Order Section.

    Returns
    -------
    :obj:`plotly.graph_objs`
        Returns a plotly/Dash graph_object/figure, consisting of data and layout.
        See https://plot.ly/ for detailed info.

    """
    fig = subplots.make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        subplot_titles=("Amplitude", "Phase"),
        print_grid=False,
    )
    servoDesign = DEVICE.servoDesign
    fig.update_xaxes(exponentformat="e", tick0=0, tickmode="linear", dtick=1)
    fig.update_xaxes(type="log")
    fig["layout"]["yaxis1"].update(title="Amplitude (dB)")
    fig["layout"]["yaxis2"].update(title="Phase (Hz)")
    fig["layout"].update(title="Transfer Function")
    fig["layout"].update(showlegend=False)
    # return an empty figure if no filters exist in ServoDesign - needed to make plot appear empty.
    # Preventing the update would keep the previous figure.
    if servoDesign.is_empty():
        return {}
    df = servoDesign.plot(plot=False)
    fig.add_trace(
        go.Scattergl(x=df.index, y=df["Servo A"], marker=dict(color=THEME[0])), 1, 1
    )
    fig.add_trace(
        go.Scattergl(x=df.index, y=df["Servo P"], marker=dict(color=THEME[1])), 2, 1
    )
    if "Servo+TF A" in df:
        fig.add_trace(
            go.Scattergl(x=df.index, y=df["Servo+TF A"], marker=dict(color=THEME2[0])),
            1,
            1,
        )
        fig.add_trace(
            go.Scattergl(x=df.index, y=df["Servo+TF P"], marker=dict(color=THEME2[1])),
            2,
            1,
        )
    return fig


def callFilterDescription(  # pylint: disable=unused-argument,too-many-branches
    dropdown, main, sec, filterIndex
):
    """Updates the filter description labels in the Second Order Section of the UI
    when the dropdown selection (filter type) changes.

    Parameters
    ----------
    dropdown : :obj:`String`
        Value passed by the dropdown. Filter type as a string.
    main : :obj:`String`
        Main filter parameter. Contents of the UI input as a string. None if empy.
    sec : :obj:`String`
        Secondary filter parameter. Contentes of the UI input as a string. None if empy.
    filterIndex : :obj:`int`
        Index of the filter in the :obj:`ServoDesign`.

    Returns
    -------
    :obj:`String`
        The description string if a filter type is selected or None.

    """
    if dropdown is None:
        raise PreventUpdate()

    fil = None
    for subclass in Filter.__subclasses__():
        if dropdown in subclass.__name__:
            fil = subclass
    if fil is None:
        log.warning("Could not find a filter with that name.")
        raise PreventUpdate()
    s = ""
    if main is None:
        return "Main value expected."
    try:
        main = fast_real(main, raise_on_invalid=True)
        # Checking for secInput
    except (ValueError, TypeError):
        s = "Invalid main value."
    else:
        if sec is not None:
            try:
                sec = fast_real(sec, raise_on_invalid=True)
            except (ValueError, TypeError):
                s = "Invalid secondary value."
            else:
                try:
                    s = str(fil(main, sec).description)
                except OverflowError:
                    s = f"Overflow error, inf in human_readable."
        else:
            try:
                s = str(fil(main).description)
            except OverflowError:
                # we have yet to encounter this, might be pretty safe, cant check the math right now
                s = f"Overflow error, inf in human_readable."

    return s


def _handleFilter(dropdown, main, sec, active, filterIndex):
    # Determining filter type
    fil = None
    for subclass in Filter.__subclasses__():
        if subclass.__name__ == dropdown:
            fil = subclass
    if fil is None:
        log.warning("Could not find a filter with that name.")
        raise PreventUpdate()
    log.info((dropdown, main, sec, active, filterIndex))
    servoDesign = DEVICE.servoDesign
    if main is not None:
        try:
            main = fast_real(main, raise_on_invalid=True)
        except (ValueError, TypeError) as e:
            log.warning(f"No real number input in main field, was {main}.")
            raise PreventUpdate()
    else:
        log.warning("No main parameter.")
        raise PreventUpdate()
    if sec is not None:
        try:
            sec = fast_real(sec, raise_on_invalid=True)
        except (ValueError, TypeError) as e:
            log.warning(f"No real number input in secondary field, was {sec}.")
            raise PreventUpdate()
        # only add filter with second parameter if sec was set,
        # since the filters have different default values for the secondary parameter
        # and shouldnt be overwritten with None
        servoDesign.add(fil(main, sec, enabled=bool(active)), index=filterIndex)
    else:
        # add filter with just main value
        servoDesign.add(fil(main, enabled=bool(active)), index=filterIndex)


def callFilterField(dropdown, main, sec, active, filterIndex):
    """Handle input changes for both the main and secondary parameter fields of filters in the
    Second Order Section of the UI.
    Applies the changes to :obj:`ServoDevice.servoDesign` accordingly.

    Parameters
    ----------
    dropdown : :obj:`String`
        Value passed by the dropdown. Filter type as a string.
    main : :obj:`String`
        Main filter parameter. Contents of the UI input as a string. None if empy.
    sec : :obj:`String`
        Secondary filter parameter. Contentes of the UI input as a string. None if empy.
    active : :obj:`list`
        List indicating whether a checkbox is enabled for the filter or not.
        If active contains the filter index, empty if inactive.
    filterIndex : :obj:`int`
        Index of the filter in the :obj:`ServoDesign`.

    Returns
    -------
    :obj:`String`
        Datetime string to pass to output. The output triggers a callback chain as well.

    """
    servoDesign = DEVICE.servoDesign
    if dropdown is not None:
        _handleFilter(dropdown, main, sec, active, filterIndex)
    else:
        servoDesign.remove(filterIndex)
    return str(datetime.time())


def callFilterVisible(dropdownInput):
    """Handle visibility of filter input fields and description depending on
    whether a value is selected in the dropdown. Refers to the Second Order Section of the UI.

    Parameters
    ----------
    dropdownInput : :obj:`String`
        Either filter type as a string or `None`.

    Returns
    -------
    :obj:`Dictionary`
        Dictionary containing CSS style information for Dash.
        Changes 'display' style of filter inputs to either 'none' or 'inline-block'.

    """
    if dropdownInput is not None:
        return {"display": "inline-block"}
    return {"display": "none"}


def getFilterOptions():
    """Return all possible filter types defined by the :obj:`ServoDesign` library of `openqlab`.
    Used to automate UI lists of possible filter types.

    Returns
    -------
    :obj:`list`
        List containing all possible filter types as Strings.

    """
    return Filter.__subclasses__()


def callToggleRamp(targetInput):
    """Set the ramp of ADwin to one of the possible channels.

    Parameters
    ----------
    targetInput : :obj:`int`
        Target servo channel. `False` if set to Off in the UI,
        as the servo defines the state that way.

    Returns
    -------
    :obj:`String`
        Information string as callback needs some output. Basically a dummy.

    """
    if not targetInput:
        DEVICE.servo(1).disableRamp()
        return "Disabled"
    servo = DEVICE.servo(targetInput)
    if servo.lockSearch:
        log.warning("Autolock is active, ramp was not activated.")
        return "Lock active, could not update ramp"
    if not servo.rampEnabled:
        servo.enableRamp()
    return "Ramp on channel " + str(targetInput)


def callLockState(n_clicks, servoNumber):
    """Enables the auto-lock feature on given servo.
    Ramp is not compatible with Autolock (Essentially, the autolock should be a better ramp).

    GUI wise, the button is located in the individual autolock section.

    Parameters
    ----------
    n_clicks : :obj:`bool`
        Times the button has been clicked for toggling functionality.
    servo : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`String`
        Return the new button label.

    """
    # check whether list is empty
    servo = DEVICE.servo(servoNumber)
    if n_clicks is None:
        raise PreventUpdate()
    current = servo.lockSearch
    if current:
        servo.lockSearch = 0
    else:
        servo.lockSearch = 1  # setting state to 1 starts searching for peak
    return servo.lockSearch
    # the servo autolock function will automatically disable the ramp if it is active on that channel


def callLockButtonLabel(servoNumber):
    """Callback handle for the autolock button. Only sets the label of the button according to the current search status.

    Parameters
    ----------
    servoNumber : :obj:`int`
        The servo index.

    Returns
    -------
    :obj:`String`
        Button Label.
    """
    servo = DEVICE.servo(servoNumber)
    if servo.lockSearch:
        s = "Turn off lock"
    else:
        s = "Trigger lock"
    return s


def callLockRange(lockRange, servoNumber):
    """Sets the search range for the autolock feature of a given servo based on UI.

    Parameters
    ----------
    lockRange : :obj:`list`
        Contains floats [start, end].
    servo : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`String`
        Return new label containing information.

    """
    servo = DEVICE.servo(servoNumber)
    start = lockRange[0]
    end = lockRange[1]
    if start > end:
        raise PreventUpdate("Start value should be bigger.")
    servo.lockSearchRange = [start, end]

    return f"Search from {servo.lockSearchMin:.2f} V to {servo.lockSearchMax:.2f} V"


def callLockGreater(greater, servoNumber):
    """Return a binary value signifying the test direction for the autolock criteria.

    `1`: "lock when greater than threshold,
    `0`: "lock when below threshold"

    Parameters
    ----------
    greater : :obj:`bool`
        Should be a boolean, but will also translate other options to boolean, so 5 will count as True etc., according to python's bool conversion.
    servoNumber : :obj:`int`
        The servo index.

    Returns
    -------
    :obj:`int`
        The binary value of `greater`, since all callbacks need a return. Should also signify that the write to ADwin actually worked because it gets called directly from the device.

    Raises
    ------
    PreventUpdate
        If `greater` parameter is `None`, might happen on start-up.
    """
    if greater is None:
        raise PreventUpdate()
    servo = DEVICE.servo(servoNumber)
    servo.lockGreater = greater
    return servo.lockGreater


def callLockThresholdInfo(threshold, greater, servoNumber):
    """Return a string for the UI containing information on threshold and threshold direction (`lockGreater`). If no values are passed will get the values directly from the device.

    Makes sure the current values are displayed in the UI.

    Parameters
    ----------
    threshold : :obj:`float` or :obj:`int`
        The autolock threshold value.
    greater : :obj:`bool` or :obj:`int`
        Boolean indicating the direction of the lock. Also accepts `1` or `0` instead of True/False.
    servoNumber : :obj:`int`
        The servo index.

    Returns
    -------
    :obj:`String`
        The label string.
    """
    servo = DEVICE.servo(servoNumber)
    if greater is None:
        greater = servo.lockGreater
    if threshold is None:
        threshold = servo.lockThreshold
    if greater:
        greaterstring = ">"
    else:
        greaterstring = "<"
    return f"Threshold {greaterstring}{threshold:.2f} V"


def callLockRelock(values, servo):
    """Set whether the AutoLock should relock automatically whenever falling
    above/below threshold for a given servo.

    Parameters
    ----------
    values : :obj:`list`
        As with all Dash checklists, even though this is for a single element,
        the callback input is a list. Empty list means off, none-empty means on.
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`bool`
        The relock value, since the UI requires a return.

    """
    servo = DEVICE.servo(servo)
    if values:
        servo.relock = True
    else:
        servo.relock = False
    return servo.relock


def callLockThreshold(threshold, servo):
    """Set the autolock threshold value for a servo.

    Parameters
    ----------
    value : :obj:`float`
        The threshold value.
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`int`
        The relock value, since the UI requires a return.

    """
    try:
        threshold = fast_real(threshold, raise_on_invalid=True)
    except (ValueError, TypeError):
        raise PreventUpdate("Input must be a real number.")
    if not -10 <= threshold <= 10:
        log.warning(f"Must be a value between -10 and 10, was {threshold}")
        raise PreventUpdate(f"Must be a value between -10 and 10, was {threshold}")
    servo = DEVICE.servo(servo)
    servo.lockThreshold = threshold
    return servo.lockThreshold


def callRamp(amp, freq, context, servoNumber):
    """Send ramp parameters entered in servo control section of the UI to
    the corresponding :obj:`nqontrol.Servo`.

    Parameters
    ----------
    amp : :obj:`float`
        Ramp amplitude.
    freq : :obj:`float`
        Ramp frequency.
    context : :obj:'json'
        Dash callback context. Please check the dash docs for more info.
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`String`
        UI label string describing current ramp state.

    """
    servo = DEVICE.servo(servoNumber)
    triggered = context.triggered[0]["prop_id"].split(".")[0]
    if "ramp_amp" in triggered:
        servo.rampAmplitude = amp
    if "ramp_freq" in triggered:
        servo.rampFrequency = freq
    amp = servo.rampAmplitude
    freq = servo.rampFrequency
    return f"Amplitude: {amp:.2f} V | Frequency: {freq:.2f} Hz"


def callADwinMonitor(channel, servo, card):
    """Set a ADwin hardware monitor channel.

    Parameters
    ----------
    channel : :obj:`int`
        ADwin hardware monitor channel index.
    servo : :obj:`int`
        Servo channel index.
    card : :obj:`String`
        String specify which servo signal to monitor. One of 'input', 'aux', 'output' or 'ttl'.

    Returns
    -------
    :obj:`list`
        Summary list with all the parameters that have been passed.
        Mostly used because the callback requires some output.

    """
    if servo is None or card is None:
        raise PreventUpdate()
    DEVICE.enableMonitor(channel, servo, card)
    return [channel, servo, card]
