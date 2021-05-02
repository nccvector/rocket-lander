## Rocket Lander Project

#### How to Run:
- Extract the Rocket Lander folder in the same directory as the Server.py
- Open a terminal, navigate to this project directory (Server.py location)
- Make sure the terminal is pointing in the same directory as Server.py file (optional, but make sure to try this if face any issues)
- Run Server.py using "python Server.py"

#### IMPORTANT:
Following should be the folder heirarchy

-- Root project folder

------ Server.py

------ Controller.py

------ Rocket Lander (folder)

---------- Rocket Lander.exe

Server.py automatically launches the simulation, as well as your Controller

Use W/A/S/D to manually cause disturbances on your rocket

The aim is to land the rocket safely using python
The simulator is made using Unity3D which gets control commands from a python server using sockets.

#### Custom Controller:
You are welcome to replace your Controller logic inside the Controller class "get_controls" function.
The "get_controls" function receives the Rocket state [x, y, theta, x_dot, y_dot, theta_dot] and it must return the control commands [fN, fT]

fN is the upwards thrust of main engine
fT is the lateral thrust that makes the Rocket turn
