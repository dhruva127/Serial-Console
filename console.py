import serial
import threading
import sys

PORT = "COM1"      # change to your COM port
BAUD = 1234 # change speed

ser = serial.Serial(
    port=PORT,
    baudrate=BAUD,
    timeout=1
)

def reader():
    while True:
        try:
            data = ser.read(1024)
            if data:
                print(data.decode(errors="ignore"), end="")
        except Exception as e:
            print("\n[Disconnected]", e)
            break

threading.Thread(target=reader, daemon=True).start()

try:
    while True:
        line = sys.stdin.readline()
        ser.write(line.encode())
except KeyboardInterrupt:
    ser.close()
