# Special thanks to sidb on the Raspbery Pi forums who's code we worked with a bit.

import smbus
import time

#======================================================================
# Dexter Industries Nintendo Wii Nunchuck Class
# http://www.dexterindustries.com/BrickPi
#======================================================================

class diwii :

	global wii_value_0
	global wii_value_1
	global wii_value_2
	global wii_value_3
	global wii_value_4
	global wii_value_5
	
	def __init__(self):
		self.address = 0x52
		self.bus = smbus.SMBus(1)


	@staticmethod
	def setup_wii(self):
		self.bus.write_byte_data(0x52, 0x40, 0x00)
		time.sleep(0.1)
	
	def UpdateWiiValues(self):
		global wii_value_0
		global wii_value_1
		global wii_value_2
		global wii_value_3
		global wii_value_4
		global wii_value_5
		self.bus.write_byte(0x52, 0x00)
		time.sleep(0.1)	
		wii_value_0 = self.bus.read_byte(0x52)
		wii_value_1 = self.bus.read_byte(0x52)
		wii_value_2 = self.bus.read_byte(0x52)
		wii_value_3 = self.bus.read_byte(0x52)
		wii_value_4 = self.bus.read_byte(0x52)
		wii_value_5 = self.bus.read_byte(0x52)
		
		
	def joyx(self):
		global wii_value_0
		return wii_value_0
	
	def joyy(self):
		global wii_value_1	
		return wii_value_1

	def accel_x(self):
		global wii_value_2, wii_value_5
		return (wii_value_2 << 2) + ((wii_value_5 & 0x0c) >> 2)
		
	def accel_y(self):
		global wii_value_3, wii_value_5
		return (wii_value_3 << 2) + ((wii_value_5 & 0x30) >> 4)

	def accel_z(self):
		global wii_value_4, wii_value_5
		return (wii_value_4 << 2) + ((wii_value_5 & 0xc0) >> 6)
	
	
	def buttons(self):
		global wii_value_5
		return wii_value_5 & 0x03

	def button_c(self):
		global wii_value_5
		buttons = wii_value_5 & 0x03
		return (buttons == 0) or (buttons == 1)

	def button_z(self):
		global wii_value_5
		buttons = wii_value_5 & 0x03
		return (buttons == 0) or (buttons == 2)


if __name__=='__main__':
	try:
		bus = diwii(address = 1)
		print "Default I2C bus is accessible"
	except:
		print "Error accessing default I2C bus"
