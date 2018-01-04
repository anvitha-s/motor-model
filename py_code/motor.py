import numpy as np
import matplotlib.pyplot as plt

import potential

dt=0.01

class Motor:
    def __init__(self,x_init,potential1,potential2,t_p,t_jump,init_state,w12,w21):
        self.state = 1
        self.x = []
        self.x.append(float(x_init))
        self.pot = [potential1,potential2]
        self.time_period = t_p
        self.transition_time = t_jump
        self.state = [init_state]
        self.w12 = w12
        self.w21 = w21
    
    def step_incr(self,x,F_ext):              
        s=np.random.normal(0,1)
        x_p = x + ((2*dt)**(0.5))*s
        x_p = x_p +  self.pot[self.state[-1]-1].incr(x)*dt - F_ext*dt
        return x_p

    def increment_x(self,F_ext):
        force_ext = F_ext
        s = np.random.uniform(0,1)
        if self.state[-1] == 1:
            if s < self.w12[int(np.floor(self.x[-1]))]:
                self.state.append(2)
            else:
                self.state.append(1)
        else: 
            if s < self.w21[int(np.floor(self.x[-1]))]:
                self.state.append(1)
            else:
                self.state.append(2)
        x_p = self.step_incr(self.x[-1],force_ext)
        x_pp = self.step_incr(x_p,force_ext)
        self.x.append(float((x_p + x_pp)/2))

    def velocity(self):
       self.avg_velocity = float((self.x[0] - self.x[-1])/(dt*len(self.x)))
       return self.avg_velocity
    
    def plotposition(self):
        x_plot = np.linspace(0, 10, num=1000)
        plt.plot(self.x,x_plot)

    def plotpos_state(self):
        self.x_1 = []
        self.x_2 = []
        self.t_1 = []
        self.t_2 = []
        for i in range(len(self.x)-1):
            if self.state[i] == 1:
                self.x_1.append(self.x[i])
                self.t_1.append(i*dt)
            if self.state[i] == 2:
                self.x_2.append(self.x[i])
                self.t_2.append(i*dt)
        plt.plot(self.x_1,self.t_1,'r.',self.x_2,self.t_2,'b.')

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
