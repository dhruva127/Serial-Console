# Serial-Console 

This Python script implements a simple command-line serial terminal. It opens a specified COM port with a defined baud rate, continuously reads data from the serial device in a background thread, and displays the output in real time. User input from the console is sent directly to the device, allowing interactive communication similar to a basic serial console.

## How Data Flows (Conceptually)
```
Keyboard ──► stdin ──► ser.write() ──► Device

Device  ──► ser.read() ──► print() ──► Screen
```
# Legal Notice:

This tool is intended for use only with devices that you own or are explicitly authorized to access and test. Unauthorized access to serial interfaces, embedded systems, or connected hardware may violate local laws, regulations, or organizational policies. The author assumes no responsibility for misuse of this software script.
