"""App dependencies"""
import dash

from nqontrol import settings
from nqontrol.servoDevice import ServoDevice

DEVICE = ServoDevice(
    deviceNumber=settings.DEVICE_NUM, readFromFile=settings.SETTINGS_FILE
)

app = dash.Dash(__name__)
