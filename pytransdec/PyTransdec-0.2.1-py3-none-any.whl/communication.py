from cv2 import COLOR_RGB2BGR, cvtColor, imshow, imwrite, rectangle, waitKey
from errno import EEXIST
from os import makedirs, walk
from typing import Dict, List, Tuple, Union

import numpy as np
from mlagents.envs import UnityEnvironment, BrainInfo
from pandas import DataFrame
from tqdm import tqdm

from .definitions import OBSERVATIONS, CAMERA_FOCUS, RESET_KEYS, TORPEDO, BALL_GRAPPER
#from rpi_communication.definitions import RPI_COMM_DICT

#from rpi_comm import RPi_Communication


class ObservationTypeNotFound(Exception):
	pass


class ResetKeyNotFound(Exception):
	pass


class WrongActionValue(Exception):
	pass


class TransdecCommunication:
	"""
	Python-Unity3D communication class
	requires latest version of TransdecEnvironment (https://github.com/PiotrJZielinski/TransdecEnvironment)
	"""

	def __init__(self, file_name: str = None, worker_id: int = 0):
		"""
		:param file_name: env file
		:param worker_id: for more than 1 parallel worker
		"""
		self.env = UnityEnvironment(file_name=file_name, worker_id=worker_id)
		self.def_brain = self.env.brain_names[0]
		self.brain = self.env.brains[self.def_brain]
		self.info: BrainInfo = None
		self.margin = 0

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.env.close()

	def reset(self, message: Dict = None, training: bool = True):
		"""reset the environment
		:param message: a dictionary defining a reset message;
		available keys are: 'CollectData' : {0, 1}, 'EnableNoise' : {0, 1}, 'Positive' : {0, 1},
												'WaterCurrent' : {0, 1}, 'FocusedObject' : {0, ..., 6}, 'EnableBackgroundImage': {0, 1}
		:param training: run environment in train mode
		"""
		if not message:
			message = {}
		if not all(k in RESET_KEYS for k in message.keys()):
			raise ResetKeyNotFound(
				"Incorrect message. Check documentation for available reset keys.")
		self.info = self.env.reset(train_mode=training, config=message)[
			self.def_brain]
		self.step()

	def step(self, action: List[float] = None):
		"""make a step
		:param action: action to be taken; 4 floats in range <-1, 1> defining x, y, z and yaw velocity
																		   5 float is camera information, 0 - front camera, 1 - bottom camera
		"""
		if not action:
			action = [0.0, 0.0, 0.0, 0.0, CAMERA_FOCUS['front_camera'],
					  TORPEDO['OFF'], BALL_GRAPPER['ON']]
		if any(abs(a) > 1.0 for a in action):
			raise WrongActionValue("Only actions in range <-1, 1> allowed.")
		self.info = self.env.step(action)[self.def_brain]

	@property
	def reward(self) -> float:
		"""get current reward
		:return: reward value
		"""
		return self.info.rewards

	def _convert_coords(self, data: Dict) -> Dict:
		"""convert data from unity env to x, y, w, h, p
		:param data: Dict from Unity env converted using built-in vector property function
		:return: same Dict with appropriate bounding box parameters
		"""
		shape = self.visual[0].shape
		# check if each value are inside of the image
		x1 = min(max(0, data['bounding_box_x']), shape[1] - 1)
		y1 = min(max(0, data['bounding_box_y']), shape[0] - 1)
		x2 = min(max(0, data['bounding_box_w']), shape[1] - 1)
		y2 = min(max(0, data['bounding_box_h']), shape[0] - 1)
		p = data['bounding_box_p']
		x = float(x1 + (x2 - x1) / 2)
		y = float(y1 + (y2 - y1) / 2)
		w = float(x2 - x1 + 2 * self.margin)
		h = float(y2 - y1 + 2 * self.margin)
		data['bounding_box_x'] = x
		data['bounding_box_y'] = y
		data['bounding_box_w'] = w
		data['bounding_box_h'] = h
		data['bounding_box_p'] = int(p)
		return data

	@property
	def vector(self) -> Dict:
		"""get current vector observations
		:return: current vector observations converted to a Dict
		"""
		observations = self.info.vector_observations[0]
		assert len(observations) == len(
			OBSERVATIONS.values()), "Vector observation length is different from the preset."
		ret = {}
		for i, data in enumerate(OBSERVATIONS.values()):
			ret[data] = observations[i]
		ret = self._convert_coords(ret)
		return ret

	@property
	def visual(self) -> List[np.ndarray]:
		"""get current visual observations
		:return: all visual observations in RGB format (0:255)
		"""
		return [(255 * img[0, :, :, :]).astype(np.uint8) for img in self.info.visual_observations]

	@staticmethod
	def _pad_filename(n: int, file_type: str = 'png', n_digits: int = 4) -> str:
		"""pad filename number with defined number of zeros
		:param n: number to be padded
		:param file_type: file type to be appended
		:return: padded filename
		"""
		return f'{n}'.zfill(n_digits) + f'.{file_type}'

	def collect_data(self, positive: bool, add_noise: bool,
					 add_background: bool, n_images: int, force_to_save_as_negative: bool = False, save_dir: str = 'collected_data',
					 start_num: int = 1, annotation_margin: float = 0.01, object_number=0,
					 used_observations: Union[str, Tuple[str, ...]] = ('x', 'y', 'w', 'h', 'p'), show_img: bool = False,
					 draw_annotations: bool = False, print_annotations: bool = False, progress_bar: bool = True):
		"""automatically collect data from Transdec Environment
		:param positive: fetch positive examples
		:param force_to_save_as_negative: force to save example as negative 
		:param add_noise: include other objects in images
		:param add_background: generate image as background (transdec environment disappears)
		:param n_images: number of images to be collected
		:param save_dir: directory for the data
		:param start_num: starting number for the filename
		:param annotation_margin: margin added to image annotations
		:param object_number: object to make dataset possible choice
		available objects are: 'Gate' : 0, 'Crucifix' : 1, 'garlic' : 2, 'vampire in coffin': 3, 'coffin': 4, 'garlic whole object': 5, 
		'Crucifix whole object' : 6, 'drop garlic': 7
		:param used_observations: observations to be saved in annotations.csv file ('all' or any of:
		'a_x', 'a_y', 'a_z', 'eps_x', 'eps_y', 'eps_z', 'phi_x', 'phi_y', 'phi_z', 'd', 'x', 'y', 'w', 'h', 'p',
		'relative_x', 'relative_y', 'relative_z', 'relative_yaw'
		:param show_img: show saved image in a window
		:param draw_annotations: draw bounding box on the showed image (has effect only when show_img == True)
		:param print_annotations: print bounding box parameters in the console
		:param progress_bar: print progress bar in the console
		"""
		self.margin = annotation_margin
		if used_observations == 'all':
			used_observations = tuple(OBSERVATIONS.keys())
		if not all(o in OBSERVATIONS.keys() for o in used_observations):
			raise ObservationTypeNotFound(
				"Incorrect used_observations. Check documentation for available observations")
		# create saving directory
		try:
			makedirs(save_dir)
		except OSError as e:
			if e.errno != EEXIST:
				raise
		# check already existing files
		files = [f for f in next(walk(save_dir))[2] if '.png' in f]
		if files:
			start_num = max([int(f[:-4]) for f in files]) + 1
		# prepare array for collected observations
		annotations = np.zeros(
			(n_images, len(used_observations) + 1), dtype=object)
		# reset environment accordingly
		reset_dict = {'CollectData': 1,
					  'EnableNoise': 1 if add_noise else 0,
					  'Positive': 1 if positive else 0,
					  'FocusedObject': object_number,
					  'EnableBackgroundImage': 1 if add_background else 0,
					  'ForceToSaveAsNegative': 1 if force_to_save_as_negative else 0
					  }
		self.reset(reset_dict)
		print(f"Collecting {n_images} images from Unity environment")
		if progress_bar:
			iterator = tqdm(range(n_images))
		else:
			iterator = range(n_images)
		for i in iterator:
			num = start_num + i
			filename = self._pad_filename(num)
			self.step()
			observations = [filename] + [self.vector[OBSERVATIONS[o]]
										 for o in used_observations]
			img = cvtColor(self.visual[0], COLOR_RGB2BGR)
			img_dimensions = img.shape
			img_height = img_dimensions[0]
			img_width = img_dimensions[1]
			imwrite(f'{save_dir}/{filename}', img)
			self.write_to_file(save_dir, filename, object_number)
			if print_annotations:
				print(observations)
			if show_img:
				if draw_annotations:
					start_point = (int((self.vector['bounding_box_x'] - self.vector['bounding_box_w'] / 2) * img_width),
								   int((self.vector['bounding_box_y'] - self.vector['bounding_box_h'] / 2) * img_height))
					end_point = (int((self.vector['bounding_box_x'] + self.vector['bounding_box_w'] / 2) * img_width),
								 int((self.vector['bounding_box_y'] + self.vector['bounding_box_h'] / 2) * img_height))
					color = (0, 0, 255)
					rectangle(img, start_point, end_point, color)
				imshow('input', img)
				waitKey(1)
			annotations[i] = observations
		# prepare dataframe for saving images
		df = DataFrame(data=annotations, columns=(
			'filename',) + used_observations)
		df.index += start_num - 1
		# save annotations
		if files:
			with open(f'{save_dir}/annotations.csv', 'a') as f:
				df.to_csv(f, header=False, index=False)
		else:
			with open(f'{save_dir}/annotations.csv', 'w') as f:
				df.to_csv(f, header=True, index=False)
		print(f'Saved {n_images} images with annotations')

	def write_to_file(self, file_directory: str, file_name: str, class_num: str):
			
		file = open(f'{file_directory}/{file_name}.txt', 'w')
		file.write(
			f"{class_num} {self.vector['bounding_box_x']} {self.vector['bounding_box_y']} {self.vector['bounding_box_w']} {self.vector['bounding_box_h']}")
		file.close()

if __name__ == '__main__':
	#rpi_comm = RPi_Communication()

	with TransdecCommunication() as tc:
		tc.reset()

		'''
		# COLLECT DATA EXAMPLE
		for i in range(0, 1):
			tc.collect_data(positive=True, add_noise=True, add_background=False, n_images=100, save_dir='collected_data/{}/train'.format(i),
							used_observations='all', object_number=i, show_img=True, draw_annotations=True)
			tc.collect_data(positive=True, add_noise=False, add_background=False, n_images=3000, save_dir='collected_data/{}/train'.format(i),
							used_observations='all', object_number=i, show_img=False, draw_annotations=True)
			tc.collect_data(positive=False, add_noise=True, add_background=False, n_images=1000, save_dir='collected_data/{}/train'.format(i),
							used_observations='all', object_number=i, show_img=False, draw_annotations=True)
			tc.collect_data(positive=True, add_noise=False, add_background=False, n_images=1000, save_dir='collected_data/{}/valid'.format(i),
							used_observations='all', object_number=i, show_img=False, draw_annotations=True)
			tc.collect_data(positive=True, add_noise=True, add_background=False, n_images=500, save_dir='collected_data/{}/valid'.format(i),
							used_observations='all', object_number=i, show_img=False, draw_annotations=True)
			tc.collect_data(positive=False, add_noise=True, add_background=False, n_images=500, save_dir='collected_data/{}/valid'.format(i),
							used_observations='all', object_number=i, show_img=False, draw_annotations=True)
		'''
		# STEERING EXAMPLE WITHOUT SENDING DATA TO RPI
		while(True):
			for i in range(100):
				# move forward, front camera is enabled
				tc.step([1, 0, 0, 0, 0, 0, 0])
			for i in range(100):
				# move backwards, bottom camera is enabled
				tc.step([-1, 0, 0, 0, 1, 0, 0])

		# STEERING EXAMPLE WITH SENDING DATA TO RPI
		while(True):
			for i in range(100):
				# move forward, front camera is enabled
				tc.step([1, 0, 0, 0, 0, 0, 0])
				#rpi_comm.send_to_rpi(tc.vector)  # send data to rpi
			for i in range(100):
				# move backwards, bottom camera is enabled
				tc.step([-1, 0, 0, 0, 1, 0, 0])
				#rpi_comm.send_to_rpi(tc.vector)  # send data to rpi
