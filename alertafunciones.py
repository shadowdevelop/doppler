import sys
import time
import serial
import logging

def enviarmensaje(mensaje):
    serial_mensaje = serial.Serial() 
    serial_mensaje = serial.Serial(
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1,
        writeTimeout=2
    )

    serial_mensaje.port = "/dev/ttyUSB0"  # good for linux
    serial_mensaje.open()
    serial_mensaje.flushInput()
    serial_mensaje.flushOutput()

    serial_mensaje.write(str.encode(mensaje))


#enviarmensaje("","")