import numpy as np
import matplotlib.pyplot as plt

import potential

dt=0.01

class Motor:
    def __init__(self,x_init,potential1,potential2,t_p,t_jump):
        self.state = 1
        self.x = []
        self.x.append(float(x_init))
        self.pot_1 = potential1
        self.pot_2 = potential2
        self.time_period = t_p
        self.transition_time = t_jump
        self.state = []

    def increment_x(self):
        print 'in increment'
        x_p = self.step_incr(self.x[-1])
        x_pp = self.step_incr(x_p)
        self.x.append(float((x_p + x_pp)/2))
    
    def step_incr(self,x):
       s=np.random.normal(0,1)
       x_p = x + ((2*dt)**(0.5))*s
       if ((len(self.x)*dt)%self.time_period)  < self.transition_time:
           self.state.append(1)
           x_p = x_p +  self.pot_1.incr(x)*dt
       else:
           self.state.append(2)
           x_p = x_p +  self.pot_2.incr(x)*dt
       return x_p

    def velocity(self):
       velocity = float(np.sum(x)/len(x))

    def plotposition(self):
        x_plot = np.linspace(0, 10, num=1000)
        plt.plot(self.x,x_plot)

    def plotpos_cycle(self):
        x_1 = []
        x_2 = []
        t_1 = []
        t_2 = []
        for i in range(1000):
            if self.state[i] == 1:
                x_1.append(self.x[i])
                t_1.append(dt*i)
            else:
                x_2.append(self.x[i])
                t_2.append(dt*i)
        plt.plot(x_1,t_1,'r.',x_2,t_2,'b.')

r = 1
c_I = 0.000001

def checkcollision(m1,m2):
    d = m1.x[-1] - m2.x[-1]  
    if(abs(d) < r):
        m1.x[-1]  = m1.x[-1] + np.sign(d)*c_I/(r**6)
        m1.x[-1]  = m1.x[-1] + np.sign(d)*c_I/(r**6)
