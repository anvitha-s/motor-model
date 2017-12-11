import numpy as np
class Motor:
    """Class describing paramters of a molecular motor, 
        and methods for determining position
    """
    #position of motor
    self.x = []
    #potential state
    self.state = 1
    #constructor with initial position
    def __init__(self,x_init):
        self.x.append(float(x_init))

    def increment_x(self):
        x_p = pot.step_incr(x[-1])
        x_pp = pot.step_incr(x_p)
        self.x.append(float((x_p + x_pp)/2))

   def step_incr(self):
       s=np.random.normal(0,1)
       x_p = x + ((2*dt)**(0.5))*s
       if ((len(x)%1000)%time_period)  < t_jump :
           x_p = x_p +  pot_1.incr(x)*dt
       else:
           x_p = x_p +  pot_2.incr(x)*dt

    def velocity(self):
       velocity = float(np.sum(x)/len(x))
