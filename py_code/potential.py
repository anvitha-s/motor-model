import numpy as np
import matplotlib.pyplot as plt

class Omega:
    def __init__(self,**kwargs):
        self.wavelength = 0
        if kwargs['type'] == 'uniform':
            self.value = kwargs['value']
        elif kwargs['type'] == 'dirac':
            self.wavelength = kwargs['length']
            self.value = kwargs['value']
    def shiftuniform(self):
            s = np.random.uniform(0,1)
            return (s > self.value)
    def shift(self, x):
        if self.wavelength == 0:
            return self.shiftuniform()
        else:
            if int((x*100))%(self.wavelength*100) == 0:
                return self.shiftuniform()
            else:
                return False

class Potential:
    def __init__(self, amplitude, a, wavelength, offset):
        self.amp = amplitude
        self.L = wavelength
        self.a = a*wavelength
        self.delta = offset
    
    def incr(self,x):
        if ((x - self.delta)%self.L) < self.a:
            dx = -self.amp/self.a
        else:
            dx = self.amp/(self.L-self.a)
        return dx

    def plotpot(self,color):
        self.field  = []
        self.field.append(0)
        for i in range(5):
            self.field.extend(np.linspace(self.amp/(self.a*100),self.amp,num=self.a*100))
            #print np.linspace(self.amp/(self.a*100),self.amp,num=self.a*100)
            self.field.extend(np.linspace(self.amp - (self.amp/((1-self.a)*100)),0,num=(self.L-self.a)*100))
        #print 'delta ' + repr(self.delta)
        self.field = np.roll(self.field, int(self.delta*100))
        self.field1 = self.field
        x_plot = np.linspace(2,7,num=501)
       # print self.field
        #print 'xplot ' + repr(len(x_plot))
        #print 'self.field ' + repr(len(self.field))
        plt.plot(x_plot,self.field1,color)
