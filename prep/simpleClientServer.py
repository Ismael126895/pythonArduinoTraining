import serial

arduinoData = serial.Serial('com4',115200)
while True:
    cmd = input('What Measurement Do you Want? ')
    cmd = cmd + '\r'
    arduinoData.write(cmd.encode())
    while arduinoData.inWaiting() == 0:
        pass
    dataPacket = arduinoData.readline()
    dataPacket = str(dataPacket,'utf-8')
    dataPacket = dataPacket.strip('\r\n')
    print(dataPacket)
    splitPacket=dataPacket.split(':')
    if splitPacket[0] == "Temp":
        print('The Temperature is: ', float(splitPacket[1]),' Degrees F')
    if splitPacket[0] == "Humidity":
        print('The Humidity is: ', float(splitPacket[1]),' % Humidity')