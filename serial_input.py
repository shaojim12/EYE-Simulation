import serial
from collections import deque
import time
import threading

class Serial_input:
    def __init__(self, baud = 9600):
        self.ser = serial.Serial("/dev/ttyACM0", baud, timeout=1)
        self.ser.baudrate = baud
        self.queue = deque()
        self.ser.reset_input_buffer()

    def getSerialString(self):
        while(True):
                
            # print("start sound detect while loop")
            input1= self.ser.readline()
            if len(input1) > 3 and input1[0] == 99:
                temp_read = input1.decode('utf-8').strip()
                # temp_read = temp_read.strip()
                self.queue.append(temp_read)
                print("get from serial", temp_read)
                time.sleep(1)
    
    def sendSerialString(self, sendStr):
        sendStr += "\n"
        output1 = sendStr.encode('utf-8')
        self.ser.write(output1)

# serial_input = Serial_input()

# T_soundDetect = threading.Thread(target=serial_input.getSerialString)
# T_soundDetect.start()
    
# while(True):
#     time.sleep(3)
#     if serial_input.queue:
#         input1 = serial_input.queue.popleft()
#         print("lenth", len(input1))
#         print(input1)
#         serial_input.sendSerialString(input1)
        # if input1 != None:
        #     inputList = input1.split("_")

        #     if inputList[1] == "mode":
        #         if inputList[2] == "general":
        #             print("general")
        #         elif inputList[2] == "clinical":
        #             print("clinical")

        #     elif inputList[1] == "pupilsize":
        #         temp_size = int(inputList[2])
        #         print(temp_size)