import serial
from collections import deque
import time
import threading

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

# serial_input = Serial_input()

# T_soundDetect = threading.Thread(target=serial_input.getSerialString)
# T_soundDetect.start()
    
# while(True):
#     time.sleep(3)
#     if serial_input.queue:
#         input1 = serial_input.queue.popleft()
#         inputList = input1.split("_")

#         if inputList[1] == "mode":
#             if inputList[2] == "general":
#                 print("general")
#             elif inputList[2] == "clinical":
#                 print("clinical")

#         elif inputList[1] == "pupilsize":
#             temp_size = int(inputList[2])
#             print(temp_size)