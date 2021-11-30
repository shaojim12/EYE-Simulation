import serial
from collections import deque


class Serial_input:
    def __init__(self, baud = 9600):
        self.ser = serial.Serial("/dev/ttyACM0", baud)
        self.ser.baudrate = baud
        self.queue = deque()


    def getSerialString(self):

        while(True):
                
            # print("start sound detect while loop")
            input1= self.ser.readline()
            # print(MIC_VAL)

            #print(MIC_VAL.decode('utf-8'))
            temp_read = input1.decode('utf-8')
            temp_read = temp_read.strip()
            self.queue.append(temp_read)
            print(temp_read)
    