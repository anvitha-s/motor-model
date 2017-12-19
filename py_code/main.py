import numpy as np
import matplotlib.pyplot as plt

import potential
import motor

V_amp = 400
a = 0.3
L = 100
p_d = 70
p1 = potential.Potential(V_amp,a,L,0)
p2 = potential.Potential(V_amp,a,L,p_d)
m1 = motor.Motor(500,p1,p2,1,0.3)
#m2 = motor.Motor(450,p1,p2,1,0.3)

for i in range(999):
    m1.increment_x()    
#    m2.increment_x()
#    motor.checkcollision(m1,m2)

print 'yaay'
m1.plotpos_cycle()
#m2.plotpos_cycle()
p1.plotpot('r')
p2.plotpot('b')
plt.show()