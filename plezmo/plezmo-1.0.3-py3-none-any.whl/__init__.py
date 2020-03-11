# Copyright (c) 2019 Gunakar Pvt Ltd
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted (subject to the limitations in the disclaimer
# below) provided that the following conditions are met:

#      * Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.

#      * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.

#      * Neither the name of the Gunakar Pvt Ltd/Plezmo nor the names of its
#      contributors may be used to endorse or promote products derived from this
#      software without specific prior written permission.

#      * This software must only be used with Plezmo elements manufactured by
#      Gunakar Pvt Ltd.

#      * Any software provided in binary or object form under this license must not be
#      reverse engineered, decompiled, modified and/or disassembled.

# NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY
# THIS LICENSE. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from plezmo.plezmo_api import PlezmoApi
from plezmo.elements.plezmo_distance import PlezmoDistance
from plezmo.elements.plezmo_motor import PlezmoMotor
from plezmo.elements.plezmo_color import PlezmoColor
from plezmo.elements.plezmo_light import PlezmoLight
from plezmo.elements.plezmo_motion import PlezmoMotion
from plezmo.elements.plezmo_display import PlezmoDisplay
from plezmo.elements.plezmo_music import PlezmoMusic
from plezmo.plezmo_exceptions.exceptions import *

# Initializes bluetooth communication. It detects if Plezmo wireless adapter is
# attached or not. If it is not attached, PlezmoAdapterNotFound exception is
# thrown
plezmoApi = PlezmoApi()
try:
    plezmoApi.init()
except:
    print("\nFailed to initialize Plezmo")
    quit()

# Instantiate element specific objects
Motor = PlezmoMotor(plezmoApi)
Color = PlezmoColor(plezmoApi)
Motion = PlezmoMotion(plezmoApi)
Light = PlezmoLight(plezmoApi)
Distance = PlezmoDistance(plezmoApi)
Display = PlezmoDisplay(plezmoApi)
Music = PlezmoMusic(plezmoApi)

globalHandler = None

def registerExceptionHandler(handler):
    """registerExceptionHandler(handler: FunctionName)
    Register exception handler for errors that happen in background
    For example, elements getting disconnected, uncaught exceptions in
    user's event handler code

    :param handler: Name of the handler function that will be called upon exception
    """
    global globalHandler
    globalHandler = handler
    print("global handler registered.......")

def PlezmoEventHandler(func):
    """Decorator to wrap each of the Event Handlers
        to handle Exceptions
    """
    def eventHandler(*args, **kwargs):
        global globalHandler
        try:
            func(*args, **kwargs)
        except ElementNotFoundException as e:
            if globalHandler != None:
                print("== Got exception {}".format(e))
                globalHandler(e)
            else:
                print("global handler not found.......")
                raise e

    return eventHandler
