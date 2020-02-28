from io import BytesIO
from pydub import AudioSegment
import speech_recognition as sr
from pvlv.static.settings import *
from pvlv.pvlv import BotInterface


def speech_to_text(bot: BotInterface, file, guild_id, language):

    if language != ITA:
        language = 'it-IT'
    else:
        language = 'en-EN'

    """
    Download the telegram file
    And prepare it for manipulation
    """
    raw_file = BytesIO()  # the file download needs a var where write the audio (on ram)
    raw_file = file.download(out=raw_file)
    raw_file.seek(0)  # reset the current position of the segment

    """
    Speed up the audio for a faster upload
    - create a new frame rate
    - convert the audio
    - set the frame rate for export, reducing the quality for a more light weight file
    """
    audio_segment = AudioSegment.from_ogg(raw_file)
    audio_segment = audio_segment.set_frame_rate(10000)  # reduce the quality of the audio for a faster upload
    audio = audio_segment.export(format='wav')
    audio.seek(0)

    """
    Open the segment as Audio file obj,
    and convert to text the content
    """
    r = sr.Recognizer()
    with sr.AudioFile(audio) as source:
        audio_data = r.record(source)  # read the entire audio file
        r.pause_threshold = 4.0

    try:
        text = r.recognize_google(audio_data, language=language)
    except Exception as e:
        print(e)
        text = ""

    # finally sent the transcription to the chat
    bot.reply_text(guild_id, 'Speech to text:\n{}'.format(text))
