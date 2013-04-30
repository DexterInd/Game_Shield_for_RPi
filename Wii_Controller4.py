# Special thanks to sidb on the Raspbery Pi forums who's code we worked with a bit.

import smbus
import time
from diwii import diwii

wii = diwii()

def main():
	wii.setup_wii(wii)

	while True:
		wii.UpdateWiiValues()
		#print wii.joyx()
		#print wii.joyy()
		#print wii.accel_x()
		#print wii.accel_y()
		#print wii.accel_z()
		
		print wii.button_z()
		print wii.button_c()
		print "++++++++++"

		time.sleep(0)

if __name__=='__main__':
	main()
