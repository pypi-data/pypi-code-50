from typing import Dict, List, Tuple, Union

OBSERVATIONS = {
				'a_x': 'acceleration_x',
				'a_y': 'acceleration_y',
				'a_z': 'acceleration_z',
				'eps_x': 'angular_acceleration_x',
				'eps_y': 'angular_acceleration_y',
				'eps_z': 'angular_acceleration_z',
				'phi_x': 'rotation_x',
				'phi_y': 'rotation_y',
				'phi_z': 'rotation_z',
				'd': 'depth',
				'x': 'bounding_box_x',
				'y': 'bounding_box_y',
				'w': 'bounding_box_w',
				'h': 'bounding_box_h',
				'p': 'bounding_box_p',
				'relative_x': 'relative_x',
				'relative_y': 'relative_y',
				'relative_z': 'relative_z',
				'relative_yaw': 'relative_yaw',
				'grab_state': 'grab_state',
				'is_torpedo_hit': 'is_torpedo_hit'
}

CAMERA_FOCUS = {
				'front_camera': 0,
				'bottom_camera': 1
}

BALL_GRAPPER = {
				'ON': 1,
				'OFF': 0	
}


TORPEDO = {
		'ON': 1,
		'OFF': 0	
}

RESET_KEYS = ['CollectData', 'EnableNoise', 'Positive', 'AgentMaxSteps', 'FocusedObject', 'EnableBackgroundImage', 'ForceToSaveAsNegative']