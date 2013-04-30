import smbus
import time

bus = smbus.SMBus(0)

# Nintendo Wii Address
wii_address = 0x52

setup_reg_1 = [0x40, 0x00]
setup_reg_2 = [0xFB, 0x00]
setup_reg_3 = [0x00]

def setup_wii():

	global gyro_divisor

	bus.write_i2c_block_data(wii_address, setup_reg_1)
	time.sleep(0.1)
	#bus.write_i2c_block_data(wii_address, setup_reg_2)
	#time.sleep(0.1)
	#bus.write_i2c_block_data(wii_address, setup_reg_3)
	#time.sleep(0.1)

def GetWiiValues():
	wii_return = bus.read_i2c_block_data(wii_address, 0x00, 6)
	return wii_return

def main():
	# Initialize the gyroscope and accelerometer
	setup_wii()

	while True:	
		print GetWiiValues()


#if __name__=='__main__':

main()
