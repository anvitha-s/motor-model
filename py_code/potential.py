class Potential:
    def __init__(self, amplitude, wavelength, a, offset)
        self.amp = amplitude
        self.L = wavelength
        self.a = a*L
        self.delta = offset
    def incr(self,x)
        if (x%L) < a: 
            dx = -amp/a
        else:
            dx = amp/(1-a)
        return dx
