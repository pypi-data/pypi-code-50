import serial

# Definitions
PARTY_OFF = 0x00
PARTY_ON = 	0x01
BASS = 		0x00
TREBLE = 	0x01
VOL_DOWN = 	0x00
VOL_UP = 	0x01
MUTE_TOG = 	0x02
MUTE_OFF = 	0x03
MUTE_ON = 	0x04
VOL_LVL = 	0x05

class Controller():
	# Init
	def __init__(self, dev="/dev/ttyUSB0"):
		self.control_port = serial.Serial(dev, 57600)
	
	# The checksum on the end of the payload
	def simple_checksum(self, data):
		checksum = sum(data)
		
		while checksum > 256:
				checksum -= 256
		
		return 0x100 - checksum
	
	# Send the data to the Controller
	def send(self, data):
		# Add the checksum to the data
		data.append(self.simple_checksum(data))

		# Wait until the command window open
		while True:
			# Reset the input buffer so we get what is right now
			self.control_port.reset_input_buffer()

			if self.control_port.read(1) == b'\x11':
				# Send the data
				self.control_port.write(data)
				break
	
	# Turn a zone on
	def zone_on(self, zone_id):
		# Build the command
		data = bytearray([0x55, 0x04, 0xA0, zone_id-1])

		# Send the data
		self.send(data)
	
	# Turn a zone off
	def zone_off(self, zone_id):
		# Build the command
		data = bytearray([0x55, 0x04, 0xA1, zone_id-1])

		# Send the data
		self.send(data)
	
	# Turn all zones off
	def zone_off_all(self):
		self.zone_off(0xFF)
	
	# Party control
	def party_control(self, party_state, zone_id):
		# Check if party state is 0 or 1
		if party_state != 0 and party_state != 1:
			raise BaseException("party_state must be PARTY_ON or PARTY_OFF")

		# Build the command
		data = bytearray([0x55, 0x05, 0xA2, party_state, zone_id-1])

		# Send the data
		self.send(data)
	
	# Select the source
	def select_source(self, source_id, zone_id):
		# Build the command
		data = bytearray([0x55, 0x05, 0xA2, zone_id-1, source_id-1])

		# Send the data
		self.send(data)
	
	# Set the tone (bass, trebel)
	def set_tone(self, tone_level, tone, zone_id):
		# Check if bass or treble was selected
		if tone != 0 and tone != 1:
			raise BaseException("tone must be BASS or TREBLE")

		# Build the command
		data = bytearray([0x55, 0x06, 0xA4, zone_id-1, tone, (tone_level % 0xFF) + 0x01])

		# Send the data
		self.send(data)
	
	# Emulate a button press
	def button_press(self, zone_id, source_id, key_id, address=0x00):
		# Build the command
		data = bytearray([0x55, 0x07, 0x52, zone_id-1, address-1 if address > 0 else 0, source_id-1, key_id-1])

		# Send the data
		self.send(data)
	
	# Set the audio level
	def audio_level(self, action, zone_id, volume=0):
		# Check if the action is valid
		if action not in [VOL_DOWN, VOL_UP, VOL_LVL, MUTE_TOG, MUTE_OFF, MUTE_ON]:
			raise BaseException("action must be one of these actions VOL_DOWN, VOL_UP, VOL_LVL, MUTE_TOG, MUTE_OFF, MUTE_ON")

		# Check if the volume level is valid
		if volume not in list(range(45)) + list(range(46, 81, 2)):
			raise BaseException("volume must be one of these values 0-44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80")

		# Build the command
		data = bytearray([0x55, 0x08, 0x57, 0x00, 0x00, action, volume, zone_id-1])

		# Send the data
		self.send(data)