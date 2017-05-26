#!/usr/bin/env python

import RPIO
import socket
import time

# Settings
PIN_NUMBER = 27
IMPULSE_TIME = 0.05
NET_INTERFACE = '127.0.0.1'
PORT = 32001


def init_gpio(pin_number):
    RPIO.setup(PIN_NUMBER, RPIO.OUT, initial=RPIO.LOW)


def door_open(pin_number, impulse_time):
    RPIO.output(pin_number, 1)
    time.sleep(impulse_time)
    RPIO.output(pin_number, 0)


def udp_listener(net_interface='127.0.0.1', port=32001):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((net_interface, port))
    return udp_socket


def main():
    init_gpio(PIN_NUMBER)
    udp_server = udp_listener(NET_INTERFACE, PORT)

    server_running = True
    while server_running:
        data, client_addr = udp_server.recvfrom(1024)
        door_open(PIN_NUMBER, IMPULSE_TIME)

    udp_server.close()


if __name__ == '__main__':
    main()
