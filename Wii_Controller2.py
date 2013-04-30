import smbus
import time
#import sys
#import os

bus = smbus.SMBus(1)

# Nintendo Wii Address
wii_address = 0x52
# wii_address = 0x07
# wii_address = 0xA4	#10100100
# wii_address = 0x53	
# wii_address = 0xA5	#10100101
# wii_address = 0x29

setup_reg_1 = 0x55
setup_reg_2 = 0x00
setup_reg_3 = 0x00

def setup_wii():

	#global gyro_divisor
	#setup_reg_1 = [0x00]
	bus.write_byte_data(wii_address, 0xF0, 0x55)
	time.sleep(1)
	#bus.write_byte_data(wii_address, 0x40, 0x00)
	time.sleep(1)
	#time.sleep(0.1)
	#bus.write_byte_data(wii_address, 0xFB, setup_reg_2)
	#time.sleep(0.1)
	#bus.write_byte_data(wii_address, 0x00, setup_reg_3)
	#time.sleep(0.1)

def GetWiiValues():
	wii_return = bus.read_i2c_block_data(wii_address, 0x00, 6)
	# wii_return = bus.read_byte_data(wii_address, 0x01)
	return wii_return

def main():
	#setup_wii()

	#while True:
	#	print GetWiiValues()
	#	time.sleep(0.5)

	bus.write_byte_data(0x52, 0x40, 0x00)
	time.sleep(0.1)
	while True:
		bus.write_byte(0x52, 0x00)
		time.sleep(0.1)
		print bus.read_byte(0x52)
		print bus.read_byte(0x52)
		print bus.read_byte(0x52)
		print bus.read_byte(0x52)
		print bus.read_byte(0x52)
		print bus.read_byte(0x52)
		time.sleep(1)
		print "- - - -"



#if __name__=='__main__':

main()
