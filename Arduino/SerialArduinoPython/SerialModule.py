import serial
from time import sleep

def initConnection(portNo, baudRate):
    try:
        ser = serial.Serial(portNo, baudRate)
        print("Device Connected")
        return ser

    except:
        print("Not connected")


def sendData(se, data, digits):
    myString="$"
    for d in data:
        myString += str(d).zfill(digits) #zfill - will fil the digit since we need 3 digits in this case
    try:
        se.write(myString.encode())
        print(myString)
    except:
        print("Data Transmission Failed")

def getData(ser):
    data = ser.readline()
    data = data.decode("utf-8")
    data = data.split("#")

    dataList = []
    [dataList.append(d) for d in data]
    return dataList[:-1]

if __name__ == "__main__":
    ser = initConnection("COM5", 9600)
    while True:
        sendData(ser,[30,0],4)
        sleep(1)
        sendData(ser,[0,0],4)
        sleep(1)

        #print(getData(ser))
