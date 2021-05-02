import socket
import struct
import traceback
import logging
import time
import subprocess
import numpy as np

from Controller import Controller

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

def sending_and_reciveing(controller):
    s = socket.socket()
    socket.setdefaulttimeout(None)
    print('socket created ')
    port = 60000
    s.bind(('127.0.0.1', port)) #local host
    s.listen(30) #listening for connection for 30 sec?
    print('socket listensing ... ')
    while True:
        try:
            c, addr = s.accept() #when port connected
            bytes_received = c.recv(4000) #received bytes
            
            state = np.frombuffer(bytes_received, dtype=np.float32) #converting into float array

            print(state)
            nn_output = controller.get_controls(state)

            bytes_to_send = struct.pack('%sf' % len(nn_output), *nn_output) #converting float to byte
            c.sendall(bytes_to_send) #sending back
            c.close()
        except Exception as e:
            logging.error(traceback.format_exc())
            print("error")
            c.sendall(bytearray([]))
            c.close()
            break




if __name__ == "__main__":

    # delta-time between two physics update of simulation
    dt = 0.333333

    # Instantiate the controller
    controller = Controller(dt)
    
    # launch the simulation
    subprocess.Popen([dir_path + "/Rocket Lander/Rocket Lander.exe"])

    # Start the communication
    sending_and_reciveing(controller) 