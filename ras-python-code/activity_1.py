import serial
import time
connect_count = 0

while connect_count < 10:
    try:
        ser = serial.Serial('/dev/ttyACM0', 115200, timeout = 1.0)
        print("Connected to Arduino.")
        break
    except serial.SerialException:
            print("Attempt " + str(connect_count + 1) + "Failed to connect.")
            connect_count += 1
            time.sleep(2)
            
time.sleep(3)
ser.reset_input_buffer()
print("Serial OK")

try:
    while True:
        light = input("Type 'on' to turn on the light and 'off' to turn it off: ")
        
        if light == 'on':
            ser.write("on\n".encode('utf-8'))
            print("User turned light on.")

        elif light == 'off':
            ser.write("off\n".encode('utf-8'))
            print("User turned light off.")
        else:
            print("Not a valid input.")
            continue
except KeyboardInterrupt:
        print("Connection broken.")
        ser.close()