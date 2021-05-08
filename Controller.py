import numpy as np

class Controller:

    def __init__(self, dt):
        self.dt = dt

        # Your personal control variables
        self.error = np.array([0, 0], dtype=np.float)
        self.prev_error = self.error.copy()
        self.total_error = np.array([0, 0], dtype=np.float)
        self.desired_state = np.array([1.8, 0]) # zero y and zero theta

    def get_controls(self, state):
        """
        Function receives the state vector of the rocket [x, y, theta, x_dot, y_dot, theta_dot]
        This function will be called in a loop (keeps receiving state and returning controls)
        Function must return np.array([fN, fT])
        Rocket mass is 1200 kg (intertia tensor will be available in future)
        fT positive left, negative right (max = +/- 1000 N)
        fN strictly positive upwards thrust of rockets main engine
        where fN is the normal Thrust force and fT is lateral thrust force (max = 2*mass*9.8 N)

        """

        # Error in altitude (y) and theta (yaw)
        self.error[0] = self.desired_state[0] - state[1]
        self.error[1] = self.desired_state[1] - state[2]

        self.total_error += self.error * self.dt
        diff_error = (self.error - self.prev_error) / self.dt

        # Required yDot and thetaDot to minimize the error
        req_yDot = 10 * self.error[0] + 0 * self.total_error[0] + 100 * diff_error[0]
        req_thetaDot = 5000 * self.error[1] + 10 * self.total_error[1] + 50000 * diff_error[1]

        # Making copy of this error to use in next iteration
        self.prev_error = self.error.copy()

        # initializing controls
        controls = np.array([0.0, 0.0])

        # Normal thrust force required to achieve required velocity f=ma
        # Rocket mass is 1200
        if abs(state[4]) <= 0.01:
            # Turn off on touchdown
            controls[0] *= 0.999 / self.dt
        else:
            controls[0] = 1200 * (req_yDot - state[4]) / self.dt

        # lateral force required to achieve required vel f=w x r
        controls[1] = req_thetaDot - state[5]

        # Printing rocket state and controls
        print(state)
        print(controls)

        return controls