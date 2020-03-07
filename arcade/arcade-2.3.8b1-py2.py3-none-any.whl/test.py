import soloud.soloud as soloud
import time

_audiolib = soloud.Soloud()
_audiolib.init()
_audiolib.set_global_volume(10)

wav_file = soloud.Wav()
wav_file.load("resources/music/funkyrobot.mp3")


_audiolib.play(wav_file,
               aVolume=1,
               aPan=0,
               aPaused=0,
               aBus=0)

time.sleep(5.0)
my_time = _audiolib.get_stream_time(wav_file.objhandle)
print(my_time)
