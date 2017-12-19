import numpy as np
import matplotlib.pyplot as plt

class Potential:
    def __init__(self, amplitude, a, wavelength, offset):
        self.amp = amplitude
        self.L = wavelength
        self.a = a*wavelength
        self.delta = offset
    
    def incr(self,x):
        if ((x - self.delta)%self.L) < self.a:
            print 'front'
            dx = -self.amp/self.a
        else:
            dx = self.amp/(self.L-self.a)
            print 'back'
        print x
        print (x - self.delta)%self.L
        return dx

    def plotpot(self,color):
        self.field  = []
        self.field.append(0)
        for i in range(10):
            self.field.extend(np.linspace(self.amp/self.a,self.amp,num=self.a))
            self.field.extend(np.linspace(self.amp - (self.amp/(1-self.a)),0,num=(self.L-self.a)))
            print len(self.field)
            print i
        self.field = np.roll(self.field, self.delta)
        self.field1 = self.field/40
        x_plot = np.linspace(0,1000,num=1001)
        print len(self.field)
        print x_plot.shape
        plt.plot(x_plot,self.field1,color)
