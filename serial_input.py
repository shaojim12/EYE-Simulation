import serial

ser=serial.Serial("/dev/ttyACM0", 9600)
ser.baudrate=9600

while(True):
        
    print("start sound detect while loop")
    MIC_VAL= ser.readline()
    print(MIC_VAL)

    #print(MIC_VAL.decode('utf-8'))
    temp_read = MIC_VAL.decode('utf-8')
    temp_read = temp_read.strip()
    print(temp_read)
    