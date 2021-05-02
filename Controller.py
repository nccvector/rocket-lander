import numpy as np

class Controller:

    def __init__(self, dt):
        self.dt = dt

        # Your personal control variables
        self.kp, self.ki, self.kd = 5000, 10, 10000
        self.error = np.array([0, 0], dtype=np.float)
        self.prev_error = self.error.copy()
        self.total_error = np.array([0, 0], dtype=np.float)
        self.desired_state = np.array([0, 0])

    def get_controls(self, state):
        """
        Function receives the state vector of the rocket [x, y, theta, x_dot, y_dot, theta_dot]
        This function will be called in a loop (keeps receiving state and returning controls)
        Function must return np.array([fN, fT])
        Rocket mass is 1200 kg (intertia tensor will be available in future)
        fT positive left, negative right
        fN strictly positive upwards thrust of rockets main engine (max = +/- 1000 N)
        where fN is the normal Thrust force and fT is lateral thrust force (max = 2*mass*9.8 N)

        """

        self.error = self.desired_state - state[1:3]

        self.total_error += self.error * self.dt
        diff_error = (self.error - self.prev_error) / self.dt

        req_vels = self.kp * self.error + self.ki + self.total_error + self.kd * diff_error

        self.prev_error = self.error.copy()

        controls = np.array([0.0, 0.0])

        # Fixed Normal thrust (slow decsent)
        controls[0] = 0.8 * 1200 * 9.8

        # lateral force required to achieve required vel
        controls[1] = req_vels[1] - state[5]

        return controls