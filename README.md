## Rocket Lander Project

<img src="/misc/lander.gif"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" /> 

#### -

#### Download builds from:
- https://mega.nz/folder/I1RFgQ4K#rtiw0HErLJnp6OGp00RI5w

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

## How to begin
- Use [W A S D] to take-off and cause disturbances on your rocket
- Once the rocket is in air and no keyboard keys are pressed, the python controller will take hold of the rocket

The aim is to land the rocket safely using python
The simulator is made using Unity3D which gets control commands from a python server using sockets.

## Writing Custom Controller:
You are welcome to replace your Controller logic inside the Controller class "get_controls" function.
The "get_controls" function receives the Rocket state [x, y, theta, x_dot, y_dot, theta_dot] and it must return the control commands [fN, fT]

fN is the upwards thrust of main engine
fT is the lateral thrust that makes the Rocket turn
