"""App dependencies"""
import dash

from nqontrol import ServoDevice
from nqontrol.general import settings

DEVICE = ServoDevice(
    deviceNumber=settings.DEVICE_NUM, readFromFile=settings.SETTINGS_FILE
)

app = dash.Dash(__name__)
