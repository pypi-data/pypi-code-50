from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip

class ClipMaster:
	def __init__(self):
		self._clip_ = ''
		self._target_clip_ = ''
		self._audio_ = ''

	def sec2minsec(self,second):
		sec_ = second - 60*int(second / 60)
		min_ = int(second / 60)
		return min_, sec_

	def cut_to(self, target_clip, start_time, end_time):
		ffmpeg_extract_subclip(self._clip_, start_time, end_time, targetname=target_clip)
		print("Scene "+self._clip_+" is cut from "+str(start_time)+" to "+str(end_time)+" sec as "+str(target_clip))

	def gif_to(self, target_gif, start_time, end_time):
		clip = (VideoFileClip(self._clip_).subclip((self.sec2minsec(start_time)[0], self.sec2minsec(start_time)[1]),(self.sec2minsec(end_time)[0], self.sec2minsec(end_time)[1])).resize(0.8))
		clip.write_gif(target_gif)

	def clip(self,clipname):
		self._clip_ = clipname
		return self

	def audio(self,audioname):
		self._audio_ = audioname
		return self

	def bind_to(self,videoname):
		my_clip = VideoFileClip(self._clip_)
		audio_background = AudioFileClip(self._audio_)
		final_audio = CompositeAudioClip([ audio_background])
		final_clip = my_clip.set_audio(final_audio)
		final_clip.write_videofile(videoname)