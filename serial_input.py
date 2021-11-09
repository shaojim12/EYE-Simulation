import serial


class Serial_input:
    def __init__(self, baud = 9600):
        self.ser = serial.Serial("/dev/ttyACM0", baud)
        self.ser.baudrate = baud

while(True):
        
    # print("start sound detect while loop")
    input1= ser.readline()
    # print(MIC_VAL)

    #print(MIC_VAL.decode('utf-8'))
    temp_read = input1.decode('utf-8')
    temp_read = temp_read.strip()
    print(temp_read)
    