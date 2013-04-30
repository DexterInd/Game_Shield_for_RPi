# Special thanks to sidb on the Raspbery Pi forums who's code we worked with a bit.

import smbus
import time

bus = smbus.SMBus(1)

# Nintendo Wii Address
wii_address = 0x52

setup_reg_1 = 0x55
setup_reg_2 = 0x00
setup_reg_3 = 0x00

# Wii Values
joyx = 0
joyy = 0

def setup_wii():
	bus.write_byte_data(0x52, 0x40, 0x00)
	time.sleep(0.1)

def UpdateWiiValues():
	bus.write_byte(0x52, 0x00)
	time.sleep(0.1)	
	wii_value_0 = bus.read_byte(0x52)
	wii_value_1 = bus.read_byte(0x52)
	wii_value_2 = bus.read_byte(0x52)
	wii_value_3 = bus.read_byte(0x52)
	wii_value_4 = bus.read_byte(0x52)
	wii_value_5 = bus.read_byte(0x52)
	
	joyx = wii_value_0
	joyy = wii_value_1

	# print "Joy X = " + str(joyx)
	# print "Joy Y = " + str(joyy)

	accel_x = (wii_value_2 << 2) + ((wii_value_5 & 0x0c) >> 2)
	accel_y = (wii_value_3 << 2) + ((wii_value_5 & 0x30) >> 4)
	accel_z = (wii_value_4 << 2) + ((wii_value_5 & 0xc0) >> 6)

	#print "Accel X: " + str(accel_x)
	#print "Accel Y: " + str(accel_y)
	#print "Accel Z: " + str(accel_z)

	buttons = wii_value_5 & 0x03
	button_c = (buttons == 0) or (buttons == 1)
	button_z = (buttons == 0) or (buttons == 2)

	print "Buttons: " + str(buttons)
	print "Button c: " + str(button_c)
	print "Button z: " + str(button_z)

	
	print "- - - -"

	# return wii_return

def main():
	setup_wii()

	while True:
		UpdateWiiValues()
		time.sleep(0.5)

#if __name__=='__main__':

main()
