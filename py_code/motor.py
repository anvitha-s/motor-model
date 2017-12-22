import numpy as np
import matplotlib.pyplot as plt

import potential

dt=0.01

class Motor:
    def __init__(self,x_init,potential1,potential2,t_p,t_jump,init_state):
        self.state = 1
        self.x = []
        self.x.append(float(x_init))
        self.pot = [potential1,potential2]
        self.time_period = t_p
        self.transition_time = t_jump
        self.state = [1]
        self.velocity = []

    def increment_x(self):
        x_p = self.step_incr(self.x[-1])
        x_pp = self.step_incr(x_p)
        self.x.append(float((x_p + x_pp)/2))
    
    def step_incr(self,x):
       s=np.random.normal(0,1)
       x_p = x + ((2*dt)**(0.5))*s
       if ((len(self.x)*dt)%self.time_period)  < self.transition_time:
           self.state.append(1)
           x_p = x_p +  self.pot[0].incr(x)*dt
       else:
           self.state.append(2)
           x_p = x_p +  self.pot[1].incr(x)*dt
       return x_p

    def increment_x(self,w12,w21=None):
        if w21 != None: 
            s = np.random.uniform(0,1)
            if self.state[-1] == 1:
                if s < w12:
                    self.state.append(2)
                else:
                    self.state.append(1)
            else: 
                if s < w21:
                    self.state.append(1)
                else:
                    self.state.append(2)
            x_p = self.step_incr(self.x[-1],self.state)
            x_pp = self.step_incr(x_p,self.state)
            self.x.append(float((x_p + x_pp)/2))
    
        else:
            if ((np.floor(self.x[-1] - self.pot[0].delta))%self.pot[0].L) == 0:
                self.increment_x(w12,0)
            elif ((np.floor(self.x[-1] - self.pot[1].delta))%self.pot[1].L) == 0:
                self.increment_x(0,w12)
            else:
                self.increment_x(0,0)
    
    def step_incr(self,x,state):              
        s=np.random.normal(0,1)
        x_p = x + ((2*dt)**(0.5))*s
        x_p = x_p +  self.pot[self.state[-1]-1].incr(x)*dt
        return x_p
    
    def velocity(self):
       self.avg_velocity = float((x[0] - x[-1])/(dt*len(self.x)))

    def plotposition(self):
        x_plot = np.linspace(0, 10, num=1000)
        plt.plot(self.x,x_plot)

    def plotpos_state(self):
        x_1 = []
        x_2 = []
        t_1 = []
        t_2 = []
        for i in range(len(self.x)-1):
            if self.state[i] == 1:
                x_1.append(self.x[i])
                t_1.append(i*dt)
            if self.state[i] == 2:
                x_2.append(self.x[i])
                t_2.append(i*dt)
        plt.plot(x_1,t_1,'r.',x_2,t_2,'b.')

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
