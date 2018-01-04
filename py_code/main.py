import numpy as np
import matplotlib.pyplot as plt

import potential
import motor

def omegagenerator(**kwargs):
    if kwargs['type'] == 'uniform':
        w = [kwargs['value']]*(kwargs['length'] + 1)
    elif kwargs['type'] == 'dirac':
        w = []
        for i in range(int(kwargs['length']/kwargs['peak'])):
            w = np.append(w,[kwargs['value']])
            w = np.append(w,[0]*(kwargs['peak'] - 1))
            print i
        if kwargs['p_d'] == 0 and kwargs['length']%kwargs['peak'] == 0:
            w = np.append(w,kwargs['value'])
        else: 
            w = np.roll(w,kwargs['p_d'])            
    return w

V_amp = 600
a = 0.3
L = 100
p_d = 40
F = 8

p1 = potential.Potential(V_amp,a,L,0)
p2 = potential.Potential(V_amp,a,L,p_d)
w12 = omegagenerator(type='dirac',value=1,p_d=0,length=1000,peak=L)
w21 = omegagenerator(type='dirac',value=1,p_d=p_d,length=1000,peak=L)
m1 = motor.Motor(500,p1,p2,1,0.3,1,w12,w21)
m2 = motor.Motor(490,p1,p2,1,0.3,1,w12,w21)

for i in range(999):
     m1.increment_x(F)
     m2.increment_x(F)
     motor.checkcollision(m1,m2)
print 'motor 1 : velocity = ' + repr(m1.velocity())
print 'motor 2 : velocity = ' + repr(m2.velocity())
m1.plotpos_cycle()
m1.plotpos_state()
m2.plotpos_state()
m2.plotpos_cycle()
p1.plotpot('r')
p2.plotpot('b')
plt.show()
