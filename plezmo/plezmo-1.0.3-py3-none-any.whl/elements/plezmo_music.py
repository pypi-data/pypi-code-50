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

from enum import Enum

from plezmo.elements.plezmo_element import PlezmoElementImpl, PlezmoElement, EventListenerWrapper
from plezmo.elements.element_types import PlezmoElementType
from ..utils.logger import Logger
from ..utils.constants import Constants
from ..utils.msg_helper import PlezmoMsg
from ..plezmo_exceptions.exceptions import *

class PlezmoMusic(PlezmoElement):

    def playAudio(self, elementName, audio):
        """playAudio(elementName: String, clipName: Audio)
        Play an audio clip on music

        :param elementName: Name of the element
        :param clipName: Audio clip to be played. (For example, Audio.CAT, Audio.CUSTOM_AUDIO_0 etc )
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.play_audio(audio)

    def playAudioAndContinue(self, elementName, clipName, loopMode):
        """playAudioAndContinue(elementName: String, clipName: Audio, loopMode: AudioLoop)
        Play an audio clip on music and continue program while it plays.

        :param elementName: Name of the element
        :param clipName: Audio clip to be played. (For example, Audio.CAT, Audio.CUSTOM_AUDIO_0 etc )
        :param loopMode: A clip can be played once with AudioLoop.ONCE or continuously with AudioLoop.CONTINUOUS. 
        Continuous play will be stopped when anything else is played on the same Music element, or by stopping the Music or with program end. 
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.play_audio_and_continue(clipName, loopMode)

    def playNote(self, elementName, note, beats):
        """playNote(elementName: String, note: Note, beats: float)
        Play the specified note for specified number of beats on music

        :param elementName: Name of the element
        :param note: The note to be played. Valid values are Note(48) to Note(84)
        :param beats: Number of beats (MIDI) for which to play the note.
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.play_note(note, beats)

    def startBuzzing(self, elementName):
        """startBuzzing(elementName: String)
        Start the buzzer on music

        :param elementName: Name of the element
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.start_buzzing()

    def stopBuzzing(self, elementName):
        """stopBuzzing(elementName: String)
        Stop the buzzer on music

        :param elementName: Name of the element
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.stop_buzzing()

    def setInstrument(self, elementName, instrumentName):
        """setInstrument(elementName: String, instrumentName: Instrument)
        Set the instrument on music.

        :param elementName: Name of the element
        :param instrumentName: Name of the instrument. (For example Instrument.PIANO)
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.set_instrument(instrumentName)

    def setTempo(self, elementName, tempo):
        """setTempo(elementName: String, tempo: Tempo)
        Set the tempo on music. The tempo controls how long would one beat of MIDI be.

        :param elementName: Name of the element
        :param tempo: Value of the tempo. Valid values are Tempo.SLOW, Tempo.MEDIUM and Tempo.FAST
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.set_tempo(tempo)

    def setVolume(self, elementName, volume):
        """setVolume(elementName: String, value: Volume)
        Set volume of music

        :param elementName: Name of the element
        :param value: Volume to be set. Valid values are Volume.LOW, Volume.MEDIUM and Volume.HIGH
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.set_volume(volume)

    def mute(self, elementName):
        """mute(elementName: String)
        Mute music

        :param elementName: Name of the element
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.mute()

    def unmute(self, elementName):
        """Unmute(elementName: String)
        Unmute music

        :param elementName: Name of the element
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.unmute()

    def stop(self, elementName):
        """stop(elementName: String)
        Stop the music

        :param elementName: Name of the element
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.stop()

    def getVolume(self, elementName):
        """getVolume(elementName: String) :int
        Get the current volume of music

        :param elementName: Name of the element
        :rtype: Volume
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.get_volume()

    def getTempo(self, elementName):
        """getTempo(elementName: String) :int
        Get current tempo set on the music

        :param elementName: Name of the element
        :rtype: Tempo
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.get_tempo()

    def getInstrument(self, elementName):
        """getInstrument(elementName: String) :String
        Get the number of currently set instrument on the music

        :param elementName: Name of the element
        :rtype: Instrument
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.get_instrument()

class PlezmoMusicImpl(PlezmoElementImpl):

    def __init__(self, name, mac, conn_handle, device_manager):
        super(PlezmoMusicImpl, self).__init__(name, PlezmoElementType.MUSIC, mac, conn_handle, device_manager)
        self._logger = Logger()

    def play_audio(self, audio):
        cmd_data = [0x6A, 0x00]
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(audio.value))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command)

    def play_audio_and_continue(self, clip_name, loop_mode):
        cmd_data = [0x6A, 0x00]
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(clip_name.value))
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(1)) # async flag
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(loop_mode.value))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command)

    def play_note(self, note, beats):
        cmd_data = [0x66, 0x00]
        beats = PlezmoMsg.convert_beats(beats)
        self._logger.debug("beats is {}".format(beats))
        cmd_data.extend(beats)
        cmd_data.extend(note.get_bytes())
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command)

    def start_buzzing(self):
        cmd_data = [0x6B, 0x00]
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(1))
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(126))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command)

    def stop_buzzing(self):
        cmd_data = [0x6B, 0x00]
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(0))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command)

    def set_instrument(self, instrument_name):
        cmd_data = [0x64, 0x00]
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(instrument_name.value))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command)

    def set_tempo(self, tempo):
        cmd_data = [0x63, 0x00]
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(tempo.value))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command)

    def set_volume(self, volume):
        cmd_data = [0x61, 0x00]
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(volume.value))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command)

    def mute(self):
        cmd_data = [0x69, 0x00]
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(1))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command, True)

    def unmute(self):
        cmd_data = [0x69, 0x00]
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(0))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command, True)

    def stop(self):
        cmd_data = [0x0B, 0x00]
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command, True)

    def get_volume(self):
        cmd_data = [0x60, 0x00]
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        response = self.send_cmd(command)
        if response[0] == 0:
            return response[1]
        else:
            return response[0]

    def get_tempo(self):
        cmd_data = [0x62, 0x00]
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        response = self.send_cmd(command)
        if response[0] == 0:
            return response[1]
        else:
            return response[0]

    def get_instrument(self):
        cmd_data = [0x68, 0x00]
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        response = self.send_cmd(command)
        if response[0] == 0:
            return response[1]
        else:
            return response[0]

class Audio(Enum):
    CAT = 0
    DOG = 1
    ROOSTER = 2
    HEN = 3
    DONKEY = 4
    SHEEP = 5
    BIRDS_SONG = 6
    BIRDS_CHIRPING = 7
    HAND_BELL = 8
    DING_BELL = 9
    SCHOOL_BELL = 10
    CATHEDRAL_BELL = 11
    POLICE_SIREN = 12
    FIRE_ENGINE_BELL = 13
    ALARM_1 = 14
    ALARM_2 = 15
    ALARM_3 = 16
    FUNNY_LAUGH = 17
    VILLAINISH_LAUGH = 18
    COUNTDOWN = 19
    CLAPPING = 20
    YES = 21
    NO = 22
    SCREAM = 23
    CUCKOO_CLOCK = 24
    CLOCK_TOLL = 25
    CLOCK_TICK = 26
    GRANDFATHER_CLOCK = 27
    CAR_HORN = 28
    TRAIN_HORN = 29
    WATER_SPLASH = 30
    WATER_BOILING = 31
    WIND = 32
    RAIN = 33
    SYNTH_MUSIC_LOOP_1 = 45
    SYNTH_MUSIC_LOOP_2 = 48
    PIANO_LOOP_1 = 46
    PIANO_LOOP_2 = 50
    PIANO_LOOP_3 = 51
    PIANO_LOOP_4 = 53
    DRUM_LOOP_1 = 34
    DRUM_LOOP_2 = 35
    DRUM_LOOP_3 = 39
    VIOLIN_LOOP_1 = 40
    VIOLIN_LOOP_2 = 47
    VIOLIN_LOOP_3 = 52
    HIPHOP_LOOP_1 = 41
    HIPHOP_LOOP_2 = 49
    ROCK_GUITAR_LOOP_1 = 42
    ROCK_GUITAR_LOOP_2 = 43
    ELECTRONIC_BEATS_LOOP = 44
    CHRISTMAS_BELLS_LOOP = 37
    BAGPIPES_LOOP = 38
    FUNLY_BRASS_MUSIC = 36
    BRASS_MUSIC = 54
    DRUM_ROLL = 55
    CUSTOM_AUDIO_0 = 100
    CUSTOM_AUDIO_1 = 101
    CUSTOM_AUDIO_2 = 102
    CUSTOM_AUDIO_3 = 103
    CUSTOM_AUDIO_4 = 104
    CUSTOM_AUDIO_5 = 105
    CUSTOM_AUDIO_6 = 106
    CUSTOM_AUDIO_7 = 107
    CUSTOM_AUDIO_8 = 108
    CUSTOM_AUDIO_9 = 109

class Tempo(Enum):
    SLOW = 60
    MEDIUM = 120
    FAST = 240
    @staticmethod
    def from_bytes(data):
        return Tempo(data[0])

class Instrument(Enum):
    PIANO = 0
    ELECTRIC_GRAND_PIANO = 1
    CLAVI = 7
    GLOCKENSPIEL = 9
    TUBULAR_BELLS = 14
    CHURCH_ORGAN = 19
    ACCORDION = 21
    GUITAR = 24
    GUITAR_HARMONICS = 31
    SLAP_BASS_1 = 36
    VIOLIN = 40
    SYNTH_VOICE = 54
    MUTED_TRUMPET = 59
    BRASS_SECTION = 61
    OBOE = 68
    ENGLISH_HORN = 69
    FLUTE = 73
    CHARANG_LEAD = 84
    FIFTHS_LEAD = 86
    HALO = 94
    RAIN = 96
    CRYSTAL = 98
    ATMOSPHERE = 99
    SITAR = 104
    BAGPIPE = 109
    TINKLE_BELL = 112
    REVERSE_CYMBALL = 119
    GUITAR_FRET_NOISE = 120
    BIRD_TWEET = 123
    TELEPHONE_RING = 124
    APPLAUSE = 126
    
    @staticmethod
    def from_bytes(data):
        return Instrument(data[0])

class Volume(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

    @staticmethod
    def from_bytes(data):
        return Volume(data[0])    

class Note():
    def __init__(self, val):
        self.value = val

    def get_bytes(self):
        return [self.value]

    @staticmethod
    def from_bytes(data):
        return Note(data[0])

class AudioLoop(Enum):
    ONCE = 0
    CONTINUOUS = 1