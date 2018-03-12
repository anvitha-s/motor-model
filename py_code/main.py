import numpy as np
import matplotlib.pyplot as plt

import potential
import motor

V_amp = 1
a = 0.3
L = 1
p_d = 0.4 
F_ext = -15
dt = 0.005
u_0 = 100

p1 = potential.Potential(V_amp,a,L,0)
p2 = potential.Potential(0,a,L,0)
w12 = potential.Omega(type='uniform',value=0.5,p_d=0,length=1000,peak=L*100)
w21 = potential.Omega(type='uniform',value=0.5,p_d=p_d*100,length=1000,peak=L*100)
m1 = motor.Motor(5,p1,p2,1,w12,w21)
#m2 = motor.Motor(490,p1,p2,1,0.3,1,w12,w21)

for i in range(int((10/dt) - 1)):
    if m1.increment_x(F_ext,dt,u_0) == 'out':
        break
#     m2.increment_x(F)
#     motor.checkcollision(m1,m2)

#print 'motor 2 : velocity = ' + repr(m2.velocity())
#m1.plotpos_cycle()

m1.plotpos_state()

p1.plotpot('r')
p2.plotpot('b')
vel = m1.velocity()
print 'motor 1 : velocity = ' + repr(vel)
plt.text(3,0.5,'dt = ' + repr(dt) + ', u_0 = ' + repr(u_0) + ', velocity = ' + repr(vel))
plt.show()
