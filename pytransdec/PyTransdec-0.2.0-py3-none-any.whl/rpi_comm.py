from rpi_communication.depth.depth import DepthSensor
from rpi_communication.engine.engine import EngineSlave
from rpi_communication.ahrs.ahrs import AhrsSensor
from rpi_communication.torpedo.torpedo import TorpedoActivator
from rpi_communication.ball_grapper.ball_grapper import BallGrapperActivator
from rpi_communication.definitions import DEFLOG, RPI_COMM_DICT
from rpi_communication.ports import DEPTH_DRIVER_PORT, ENGINE_SLAVE_PORT, AHRS_DRIVER_PORT, TORPEDO_FIRE_CLIENT_PORT, BALL_GRAPPER_CLIENT_PORT
from typing import Dict

import time



#engine = EngineSlave(ENGINE_SLAVE_PORT, DEFLOG.MOVEMENTS_LOCAL_LOG, 'movement', DEFLOG.LOG_DIRECTORY)

#while True:
#	print("Message: {0}".format(engine.get_movements()))

class RPi_Communication:
	def __init__(self):
		log_directory = DEFLOG.LOG_DIRECTORY
		self.engine = EngineSlave(ENGINE_SLAVE_PORT, DEFLOG.MOVEMENTS_LOCAL_LOG, 'movement', log_directory)
		self.depth_sensor = DepthSensor(DEPTH_DRIVER_PORT, DEFLOG.DEPTH_LOCAL_LOG, 'depth', log_directory)
		self.ahrs_sensor = AhrsSensor(AHRS_DRIVER_PORT, DEFLOG.AHRS_LOCAL_LOG, 'ahrs', log_directory)
		self.torpedo_activator = TorpedoActivator(TORPEDO_FIRE_CLIENT_PORT, DEFLOG.TORPEDOES_LOCAL_LOG, 'torpedo', log_directory)
		self.ball_grapper_activator = BallGrapperActivator(BALL_GRAPPER_CLIENT_PORT, DEFLOG.BALL_GRAPPER_LOCAL_LOG, 'ball_grapper', log_directory)

	def get_depth_data(self, data: Dict):
		return data['depth']

	def get_ahrs_data(self, data: Dict):
		ahrs_data = {
			RPI_COMM_DICT['acceleration_x']: data['acceleration_x'],
			RPI_COMM_DICT['acceleration_y']: data['acceleration_y'],
			RPI_COMM_DICT['acceleration_z']: data['acceleration_z'],
			RPI_COMM_DICT['angular_acceleration_x']: data['angular_acceleration_x'],
			RPI_COMM_DICT['angular_acceleration_y']: data['angular_acceleration_y'],
			RPI_COMM_DICT['angular_acceleration_z']: data['angular_acceleration_z'],
			RPI_COMM_DICT['rotation_x']: data['rotation_x'],
			RPI_COMM_DICT['rotation_y']: data['rotation_y'],
			RPI_COMM_DICT['rotation_z']: data['rotation_z']
		}
		return ahrs_data

	def send_to_rpi(self, data: Dict):
		self.depth_sensor.send_data(self.get_depth_data(data))
		self.ahrs_sensor.send_data(self.get_ahrs_data(data))
		time.sleep(0.01)

	def get_movements(self):
		return self.engine.get_movements()

	def get_torpedo_data(self):
		return self.torpedo_activator.get_torpedo_data()

	def get_ball_grapper_data(self):
		return self.ball_grapper_activator.get_ball_grapper_data()



if __name__ == '__main__':
	data = {}

	data["depth"] = 0
	data['acceleration_x'] = 0
	data['acceleration_y'] = 0
	data['acceleration_z'] = 0
	data['angular_acceleration_x'] = 0
	data['angular_acceleration_y'] = 0
	data['angular_acceleration_z'] = 0
	data['rotation_x'] = 0
	data['rotation_y'] = 0
	data['rotation_z'] = 0

	rpi_comm = RPi_Communication();
	while True:
		rpi_comm.send_to_rpi(data)
		rpi_comm.get_torpedo_data()
		time.sleep(1);
		#pass