import numpy as np
import matplotlib.pyplot as plt

import potential

class Motor:
    def __init__(self,x_init,potential1,potential2,init_state,w12,w21):
        self.x = []
        self.x.append(float(x_init))
        self.pot = [potential1,potential2]
        self.state = [init_state]
        self.w = [w12,w21]
    
    def step_incr(self,x,F_ext,dt,u_0):              
        s=np.random.normal(0,1)
        x_p = x + ((2*dt)**(0.5))*s*(self.state[-1]-1)
        x_p = x_p + u_0*self.pot[self.state[-1]-1].incr(x)*dt + F_ext*dt
        return x_p

    def increment_x(self,F_ext,dt,u_0):
        force_ext = F_ext
        self.dt = dt
        s = np.random.uniform(0,1)
        #print 'size : '
        #print int(np.floor(self.x[-1])*100)
        if self.w[self.state[-1]-1].shift(self.x[-1]):
            self.state.append(self.state[-1]%2 + 1)
        else:
            self.state.append(self.state[-1])
        #if self.state[-1] == 1:
        #    if int(np.floor(self.x[-1])*100) > 1001:
        #        return 'out' 
        #    if s < self.w12[int(np.floor(self.x[-1])*100)]:
        #        self.state.append(2)
        #    else:
        #        self.state.append(1)
        #else: 
        #    if s < self.w21[int(np.floor(self.x[-1]))]:
        #        self.state.append(1)
        #    else:
        #        self.state.append(2)
        x_p = self.step_incr(self.x[-1],force_ext,dt,u_0)
        x_pp = self.step_incr(x_p,force_ext,dt,u_0)
        self.x.append(float((x_p + x_pp)/2))

    def velocity(self):
       self.avg_velocity = float((self.x[-1] - self.x[0])/(self.dt*len(self.x)))
       return self.avg_velocity
    
    def plotposition(self):
        x_plot = np.linspace(0, 10, num=1000)
        plt.plot(self.x,x_plot)

    def plotpos_state(self):
        #self.x_1 = []
        #self.x_2 = []
        #self.t_1 = []
        #self.t_2 = []
        color = ['r','b']
        for i in range(len(self.x) - 2):
            plt.plot([self.x[i],self.x[i+1]],[i*self.dt,(i+1)*self.dt],color[self.state[i]-1])
            plt.plot(self.x[i],i*self.dt,color[self.state[i]-1] + '.')

r = 1
c_I = 0.000001

def checkcollision(m1,m2):
    d = m1.x[-1] - m2.x[-1]  
    if(abs(d) < r):
        m1.x[-1]  = m1.x[-1] + np.sign(d)*c_I/(r**6)
        m1.x[-1]  = m1.x[-1] + np.sign(d)*c_I/(r**6)
