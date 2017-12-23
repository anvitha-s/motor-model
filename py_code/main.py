import numpy as np
import matplotlib.pyplot as plt

import potential
import motor

V_amp = 600
a = 0.3
L = 100
p_d = 40
w12 = 0.2 
w21 = 0.4
F = 10
p1 = potential.Potential(V_amp,a,L,0)
p2 = potential.Potential(V_amp,a,L,p_d)
m1 = motor.Motor(500,p1,p2,1,0.3,1)
#m2 = motor.Motor(450,p1,p2,1,0.3)

for i in range(999):
     m1.increment_x(F,1)
#    m2.increment_x()
#    motor.checkcollision(m1,m2)


print 'velocity = ' + repr(m1.velocity())
#m1.plotpos_cycle()
m1.plotpos_state()
#m2.plotpos_cycle()
p1.plotpot('r')
p2.plotpot('b')
plt.show()
